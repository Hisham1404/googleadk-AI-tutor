/**
 * ============================================
 * AI Tutor - Frontend JavaScript Application
 * ============================================
 * 
 * Main JavaScript file for the AI Tutor frontend interface.
 * Handles user interactions, API communication, and real-time
 * agent workflow visualization.
 * 
 * Author: AI Tutor Team
 * Version: 1.0.0
 * 
 * Features:
 * - Real-time chat interface
 * - Agent workflow visualization
 * - Markdown formatting support
 * - Responsive UI interactions
 * - Multi-agent system coordination display
 * 
 * Dependencies:
 * - Modern ES6+ JavaScript (async/await, arrow functions)
 * - Fetch API for HTTP requests
 * - DOM manipulation APIs
 * ============================================
 */

// Wait for DOM to be fully loaded before initializing
document.addEventListener('DOMContentLoaded', () => {
    
    // ==========================================
    // DOM ELEMENT REFERENCES
    // ==========================================
    
    // Main chat interface elements
    const chatLog = document.getElementById('chat-log');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const chatWindow = document.querySelector('.chat-window');
    
    // Agent workflow visualization elements
    const thinkingPanel = document.getElementById('thinking-panel');
    const thinkingContent = document.getElementById('thinking-content');
    const thinkingCollapseBtn = document.getElementById('thinking-collapse');

    // ==========================================
    // AGENT CONFIGURATION
    // ==========================================
    
    /**
     * Agent metadata for UI representation
     * Maps agent identifiers to display properties
     */
    const agents = {
        'root': { 
            name: 'Root Orchestrator', 
            icon: 'fas fa-crown', 
            color: '#e67e22' 
        },
        'maths_agent': { 
            name: 'Mathematics Agent', 
            icon: 'fas fa-calculator', 
            color: '#3498db' 
        },
        'physics_agent': { 
            name: 'Physics Agent', 
            icon: 'fas fa-atom', 
            color: '#e74c3c' 
        },
        'chemistry_agent': { 
            name: 'Chemistry Agent', 
            icon: 'fas fa-flask', 
            color: '#27ae60' 
        },
        'news_analyst': { 
            name: 'News Analyst', 
            icon: 'fas fa-newspaper', 
            color: '#9b59b6' 
        }
    };

    // ==========================================
    // INITIALIZATION
    // ==========================================
    
    // Initialize the application interface
    initializeInterface();

    /**
     * Sets up event listeners and initial UI state
     */
    function initializeInterface() {
        // Set up thinking panel collapse functionality
        thinkingCollapseBtn.addEventListener('click', toggleThinkingPanel);
        
        // Auto-resize textarea as user types
        userInput.addEventListener('input', autoResizeTextarea);
        
        // Clear welcome message on first user interaction
        userInput.addEventListener('focus', clearWelcomeMessage, { once: true });
    }

    // ==========================================
    // UI INTERACTION FUNCTIONS
    // ==========================================

    /**
     * Toggles the visibility of the agent workflow panel
     */
    function toggleThinkingPanel() {
        thinkingPanel.classList.toggle('collapsed');
        const icon = thinkingCollapseBtn.querySelector('i');
        icon.classList.toggle('fa-chevron-up');
        icon.classList.toggle('fa-chevron-down');
    }

    /**
     * Automatically adjusts textarea height based on content
     * Maintains a maximum height to prevent excessive expansion
     */
    function autoResizeTextarea() {
        userInput.style.height = '24px';
        const scrollHeight = userInput.scrollHeight;
        const maxHeight = 120;
        
        if (scrollHeight <= maxHeight) {
            userInput.style.height = `${scrollHeight}px`;
            userInput.style.overflowY = 'hidden';
        } else {
            userInput.style.height = `${maxHeight}px`;
            userInput.style.overflowY = 'auto';
        }
    }

    /**
     * Dims the welcome message when user starts interacting
     */
    function clearWelcomeMessage() {
        const welcomeMessage = chatLog.querySelector('.welcome-message');
        if (welcomeMessage) {
            welcomeMessage.style.opacity = '0.5';
        }
    }

    // ==========================================
    // MESSAGE FORMATTING FUNCTIONS
    // ==========================================

    /**
     * Converts markdown-style text to HTML formatting
     * Supports bold, italic, code, headings, and line breaks
     * 
     * @param {string} text - Raw text with markdown syntax
     * @returns {string} HTML-formatted text
     */
    function formatMarkdown(text) {
        return text
            // Bold text: **text** or __text__
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/__(.*?)__/g, '<strong>$1</strong>')
            // Italic text: *text* or _text_ (avoiding conflicts with bold)
            .replace(/(?<!\*)\*([^\*\n]+?)\*(?!\*)/g, '<em>$1</em>')
            .replace(/(?<!_)_([^_\n]+?)_(?!_)/g, '<em>$1</em>')
            // Inline code: `text`
            .replace(/`(.*?)`/g, '<code>$1</code>')
            // Line breaks
            .replace(/\n/g, '<br>')
            // Headings (markdown-style)
            .replace(/^### (.*$)/gm, '<h3>$1</h3>')
            .replace(/^## (.*$)/gm, '<h2>$1</h2>')
            .replace(/^# (.*$)/gm, '<h1>$1</h1>');
    }

    // ==========================================
    // CHAT MESSAGE FUNCTIONS
    // ==========================================

    /**
     * Adds a new message to the chat log
     * 
     * @param {string} text - Message content
     * @param {string} sender - 'user' or 'bot'
     * @param {Object} agentInfo - Optional agent metadata for bot messages
     */
    function appendMessage(text, sender, agentInfo = null) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${sender}-message`);
        
        // Add agent badge for bot messages with agent info
        if (agentInfo) {
            const agentBadge = document.createElement('div');
            agentBadge.className = 'agent-badge';
            agentBadge.innerHTML = `<i class="${agentInfo.icon}"></i> ${agentInfo.name}`;
            messageDiv.appendChild(agentBadge);
        }
        
        const textDiv = document.createElement('div');
        
        // Apply markdown formatting for bot messages
        if (sender === 'bot') {
            textDiv.innerHTML = formatMarkdown(text);
        } else {
            textDiv.textContent = text;
        }
        
        messageDiv.appendChild(textDiv);
        chatLog.appendChild(messageDiv);
        scrollToBottom();
    }

    /**
     * Displays an animated typing indicator while processing
     * 
     * @returns {HTMLElement} The typing indicator element (for later removal)
     */
    function showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.classList.add('message', 'bot-message', 'typing-indicator');
        typingDiv.innerHTML = `
            Thinking...
            <span></span>
            <span></span>
            <span></span>
        `;
        chatLog.appendChild(typingDiv);
        scrollToBottom();
        return typingDiv;
    }

    /**
     * Removes the typing indicator from the chat
     * 
     * @param {HTMLElement} indicator - The typing indicator element to remove
     */
    function removeTypingIndicator(indicator) {
        if (indicator && indicator.parentNode) {
            chatLog.removeChild(indicator);
        }
    }

    // ==========================================
    // AGENT WORKFLOW VISUALIZATION
    // ==========================================

    /**
     * Displays a step in the agent workflow process
     * 
     * @param {string} agent - Agent identifier
     * @param {string} action - Action being performed
     * @param {string} description - Detailed description of the action
     */
    function showThinkingStep(agent, action, description) {
        // Clear placeholder if it exists
        const placeholder = thinkingContent.querySelector('.thinking-placeholder');
        if (placeholder) {
            placeholder.remove();
        }

        const stepDiv = document.createElement('div');
        stepDiv.className = 'workflow-step-item';
        
        const agentInfo = agents[agent] || agents['root'];
        
        stepDiv.innerHTML = `
            <div class="workflow-icon" style="background: linear-gradient(135deg, ${agentInfo.color}, ${agentInfo.color}dd);">
                <i class="${agentInfo.icon}"></i>
            </div>
            <div class="workflow-text">
                <div class="step-title">${action}</div>
                <div class="step-description">${description}</div>
            </div>
        `;
        
        thinkingContent.appendChild(stepDiv);
        thinkingContent.scrollTop = thinkingContent.scrollHeight;
    }

    /**
     * Resets the thinking panel to its default state
     */
    function clearThinkingPanel() {
        thinkingContent.innerHTML = `
            <div class="thinking-placeholder">
                <i class="fas fa-brain"></i>
                <p>Agent thinking process will appear here when you ask a question</p>
            </div>
        `;
    }

    /**
     * Highlights the currently active agent in the sidebar
     * 
     * @param {string} agentName - The agent to highlight
     */
    function highlightActiveAgent(agentName) {
        // Remove active class from all agent cards
        document.querySelectorAll('.agent-card').forEach(card => {
            card.classList.remove('active');
        });
        
        // Add active class to current agent
        const activeCard = document.querySelector(`[data-agent="${agentName}"]`);
        if (activeCard) {
            activeCard.classList.add('active');
        }
    }

    /**
     * Scrolls the chat window to show the latest message
     */
    function scrollToBottom() {
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    // ==========================================
    // API COMMUNICATION
    // ==========================================

    /**
     * Sends user message to the backend API and handles the response
     * Manages the complete flow: UI updates, API call, response handling
     */
    async function sendMessage() {
        const query = userInput.value.trim();
        if (query === '') return;

        // Clear welcome message completely on first interaction
        const welcomeMessage = chatLog.querySelector('.welcome-message');
        if (welcomeMessage) {
            welcomeMessage.remove();
        }

        // Display user message
        appendMessage(query, 'user');
        userInput.value = '';
        userInput.style.height = '24px';

        // Show initial thinking process
        clearThinkingPanel();
        showThinkingStep('root', 'Analyzing Query', 'Understanding the question and determining the best approach...');
        highlightActiveAgent('root');

        // Show typing indicator
        const typingIndicator = showTypingIndicator();

        try {
            // Send request to backend API
            const response = await fetch('/api/query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: query }),
            });

            // Remove typing indicator
            removeTypingIndicator(typingIndicator);

            // Handle API errors
            if (!response.ok) {
                const errorData = await response.json().catch(() => null);
                const errorMessage = errorData && errorData.response 
                                     ? errorData.response 
                                     : `Error: ${response.status} ${response.statusText}`;
                appendMessage(errorMessage, 'bot');
                showThinkingStep('root', 'Error Occurred', errorMessage);
                return;
            }

            const data = await response.json();
            
            // Simulate agent workflow based on response content
            simulateAgentWorkflow(query, data.response);
            
            // Show final response
            appendMessage(data.response, 'bot');

            // Reset agent highlighting
            setTimeout(() => {
                document.querySelectorAll('.agent-card').forEach(card => {
                    card.classList.remove('active');
                });
            }, 2000);

        } catch (error) {
            removeTypingIndicator(typingIndicator);
            console.error('Error sending message:', error);
            appendMessage('An unexpected error occurred. Please check the console.', 'bot');
            showThinkingStep('root', 'Connection Error', 'Failed to communicate with the AI system');
        }
    }

    function simulateAgentWorkflow(query, response) {
        const lowerQuery = query.toLowerCase();
        
        // Determine which agents might be involved based on keywords
        if (lowerQuery.includes('math') || lowerQuery.includes('calculate') || lowerQuery.includes('solve') || /\d+/.test(query)) {
            showThinkingStep('maths_agent', 'Mathematics Processing', 'Performing calculations and mathematical analysis...');
            highlightActiveAgent('maths');
        }
        
        if (lowerQuery.includes('physics') || lowerQuery.includes('speed') || lowerQuery.includes('light') || lowerQuery.includes('force') || lowerQuery.includes('energy')) {
            showThinkingStep('physics_agent', 'Physics Analysis', 'Looking up physical constants and applying physics principles...');
            highlightActiveAgent('physics');
        }
        
        if (lowerQuery.includes('chemistry') || lowerQuery.includes('element') || lowerQuery.includes('carbon') || lowerQuery.includes('reaction')) {
            showThinkingStep('chemistry_agent', 'Chemistry Processing', 'Analyzing chemical properties and reactions...');
            highlightActiveAgent('chemistry');
        }
        
        if (lowerQuery.includes('news') || lowerQuery.includes('ai') || lowerQuery.includes('artificial intelligence') || 
            lowerQuery.includes('latest') || lowerQuery.includes('current') || lowerQuery.includes('recent') || 
            lowerQuery.includes('development') || lowerQuery.includes('update')) {
            showThinkingStep('news_analyst', 'News Analysis', 'Searching for latest AI news and developments...');
            highlightActiveAgent('news');
        }
        
        // Final synthesis step
        setTimeout(() => {
            showThinkingStep('root', 'Synthesizing Response', 'Combining results from specialist agents into final answer...');
            highlightActiveAgent('root');
        }, 1000);
    }

    // Event listeners
    sendButton.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            sendMessage();
        }
    });

    // Example question functionality
    window.fillExample = function(exampleText) {
        userInput.value = exampleText;
        userInput.focus();
        autoResizeTextarea();
    };
});