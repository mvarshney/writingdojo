I have a project idea now. It is called "Writing Dojo", an AI agent that will help my children (12 year old and 9 year old to write). There will be several agents:

- Grading Agent: will grade the writing composition of the child, suggest improvements. Both the writing and the assessment will be stored in memory.
- Topic Suggest Agent: Will look at previous writing and assessments to suggest a topic to write.
- Coach Agent: will review the past assessments, and show how well the student is doing. And suggest strategies to get better.

This will be a react app. I will talk about the design layout later. 

For now, please ask me questions to clarify any details before we start planning the project.
----------------------

User Experience & Flow:
- Will children type directly into the app.
- We should have a time limit for writing session.
- Yes, there should be different writing modes (e.g., creative writing, essays, stories). In fact, the Topic Suggest Agent should make look into the past writings and make sure that children are writing a variety of modes.

Grading Agent:
- The grading agent will evaluate that the writing is at appropriate grade level. This includes grade appropriate grammar, structure, vocabulary. 
- Grading will be different for the 9-year-old vs. 12-year-old.
- The feedback should be detailed. It must show specific examples of improvements.

Topic Suggest Agent:
- We want children to write on variety of topics and writing modes. Personalization is good, but we want to make sure they are exposed to variety.
- No constraints or specific themes. We are aiming for variety.
- The agent must consider the child's previous performance when suggesting topics.

Coach Agent:
- We will discuss the progress metric later on.
- The coach should provide weekly/monthly progress reports.
- It can suggest writing exercises, reading recommendations)

Memory Systems:
- How long should we retain the writing samples and assessments? Forever.
- Should parents have access to view their children's progress? Yes.
- Do you want to implement any privacy features for the children's work? No.

Technical Considerations:
- Do you have a preference for the backend technology? (AutoGen can work with various backends). No preference.
- Should the app support multiple children accounts? Yes.
- Do you want to include any gamification elements to make it more engaging? We can discuss this later.

Additional Features:
- Would you like to include any collaborative features where children can share their work with family members? No.
- Should there be any rewards or achievements system? We can discuss this later.
- Do you want to include any educational resources or writing tips? No.
---------------------

Writing Interface:
- Should we include a basic text editor with formatting options? Yes.
- Do you want to include a word count feature? Yes.
- Should there be a spell-check feature? No.

Session Management:
- What should be the default time limit for writing sessions? 30 minutes.
- Should children be able to save drafts and continue later? Yes.
- Should there be a minimum word count requirement? Yes.

Grading System:
- Should we use a numerical grading system (e.g., 1-10) or descriptive grades? Descriptive.
- Do you want to include specific rubrics for different writing modes? We will discuss this later.
- Should the grading be immediate or can it be delayed? Immediate.

Progress Tracking:
- What specific metrics should we track? (e.g., word count, vocabulary diversity, grammar accuracy). All of them.
- Should we create visual progress charts? Yes.
- How detailed should the progress reports be? Simple charts.

Technical Setup:
- Do you want to use a specific database for storing the writing samples and assessments? I haven't decided yet.
- Should we implement user authentication? No.
- Do you want to include any API rate limiting for the agents? No.

-----------------

Let create a top bar. On the left there will be selection between two children: Adhvik and Anika. Adhvik is a boy, so blue color; and pink color for Anika. One child will be selected. On the right side of bar, lets have two links: Start Writing, and Show Progress. You can ask me questions if you need details.

This looks good. Can you put icons next to Start Writing and Show Progress. 
When the child's name is selected, can you gray out the other child's name.

Before the Child selection toggle button, can you add text "I am .. "

The timer can be distracting when writing. Instead of updating it every second, lets update it every minute. The timer should also start from 0 and count up.

Lets switch our focus to AI agents. How do I run the test cases?