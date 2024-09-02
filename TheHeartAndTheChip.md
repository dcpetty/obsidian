---
category: Robotics
---

I recently read *The Heart and the Chip: Our Bright Future With Robots* ([ISBN 978-1-324-05023-0](https://isbn.nu/9781324050230)) by [Daniella Rus](https://danielarus.csail.mit.edu/) &amp; Gregory Mone. I am a a roboticist and computing educator and this note captures several of my observations about this book.

- There is a definition of a robot on p. 13 and it comports with the definition towards which I always guided my students with a [*Is this a robot?*](https://docs.google.com/document/d/13irVOPcPFg7OvfBycZw4OXjkR905275ue2saTuAY-Vo/) activity each semester: 'A robot is a programmable mechanical device that takes input from its surroundings, processes that information, then takes physical action in response to that input' that engages in the 'sense - think - act' loop.
- Daniella Rus is a roboticist, so much of the book is about robots (dreams / reality / responsibility), but it is also largely about artificial intelligence (AI) and its application to physical computing and robotics and the challenges we face in its ubiquitous adoption.
- Daniella Rus is a *bone fide* nerd. In typical MIT fashion, and going against all advice for encouraging young women in engineering, she invokes comic books, science fiction, and sci-fi movies in many of her examples of robotics and AI.
- Daniella Rus is the *Director of [MIT CSAIL](https://csail.mit.edu/)* and, as such, has been involved in many inventions, has worked on many interesting projects, has taught many accomplished students, and knows tons of experts in many fields. She liberally sprinkles illustrative anecdotes with their names, research, and impact throughout the narrative. They are conveniently all listed in the afternotes.
- Rus is fundamentally a techno-optimist, so she argues *against* the [robot apocalypse](https://what-if.xkcd.com/5/) and *for* the enhancement of the human condition through robotics &mdash; where the damaging effects of greedy people or trolls are considered addressable problems. 

**I hope you read [*The Heart and the Chip: Our Bright Future With Robots*](https://isbn.nu/9781324050230)!** These notes are only *my* summary.

# Book

The book is divided in three sections: **Dreams** / **Reality** / **Responsibility**. There is an extensive **Notes** section at the end and **An Informative Technical Interlude** in the middle giving a short background on AI.

## Dreams

Chapters 1-7 (*Strength*, *Reach*, *Time*, *Lift*, *Magic*, *Vision*, *Precision*) each describe an aspect of physical reality that robots can augment with imagined, actual, and visionary examples. The examples mostly keep the human in the loop and views robots as extending human capabilities in a variety of ways. 

I was reminded of the perspective in [*Robot &amp; Frank*](https://www.imdb.com/title/tt1990314/) (2012) set '&hellip;sometime in the near future' where Robot assists the elderly and gruff Frank &mdash; who is suffering from signs of dementia &mdash; with his capers and thereby forms a bond between man and machine (heart and chip).

### Magic

Chapter 5 &mdash; the *Magic* chapter &mdash; is a reference to [Clarke's Third Law](https://en.wikipedia.org/wiki/Clarke's_three_laws#The_laws) ('Any sufficiently advanced technology is indistinguishable from magic'). 
- Rus describes ways in which, 'any shape in nature or the built environment can become a robot' and the machine learning AI algorithms required to accomplish the design and implementation of this vision &mdash; thereby firmly melding the heart and the chip.
- Rus describes various types of reconfigurable robots made of robotic 'particles' that form 'intelligent programmable matter.' (This *magic* future reminded me of the 'matter compilers' in Neal Stephenson's [*The Diamond Age*](https://en.wikipedia.org/wiki/The_Diamond_Age) and the attendant societal impacts are worth considering.)

## Reality

Chapters 8-12 (*How to build a robot*, *The brain in motion*, *The brain in touch*, *How robots learn*, *The technologist's to-do-list*) describe the components required for a robot's sense-think-act loop and what is required of AI to make the 'brain' of a robot (the *think* part) successfully achieve the goals of the human / machine collaboration.

### How to build a robot

Chapter 8 describes the layers of a robot brain consisting of cognitive-level controllers, task-level controllers, high-level controllers, and low-level controllers.

### The brain in motion

Chapter 9 describes the aspects of a robot's model of the world consisting of perception, localization, segmentation, and object recognition through the phases of reasoning, planning, and control to create a robot's configuration space.

### How robots learn

Chapter 11 introduces *deep neural networks* and their miraculous abilities and limitations. Most interesting to me is the description of [liquid neural networks](https://techcrunch.com/2023/08/17/what-is-a-liquid-neural-network-really/) (LNNs) as an alternative to the massive neural networks like those in [GPT-4](https://en.wikipedia.org/wiki/GPT-4) (which has $1.76\times10^{12}$ fixed parameters). LNNs are something I *definitely* want to look into and understand better.

### An Informative Technical Interlude

In this interlude, Rus gives an overview and definition-of-terms for the types of AI / machine learning referred to in the book.

{% comment %}

- Machine learning &mdash; A subset of AI that learns from data to identify patterns or make predictions with minimal human intervention. Using automatically built data models, computers can find hidden insights without being explicitly programmed so as to make predictions on unseen or future data. |
- Supervised learning &mdash; '&hellip;is defined by its use of human-labeled datasets to train a model&hellip; to classify data or make predictions accurately. &hellip;The goal of a supervised-learning algorithm is to learn a function that, given an input, predicts the correct output.' |
- Deep learning &mdash; A subset of machine learning with algorithms called *artificial neural networks* inspired by the brain. These networks have many layers (hence 'deep'); they are built from *artificial neurons* organized in network architectures; computed with the summation of the (fixed) weighted inputs processed through an activation function; where input features (from new data) are processed into outputs (the predictions). 'There are different types of neural network architectures, including *feed forward networks*, *convolutional networks*, *recurrent neural networks*, *long short-term memory networks (LSTM)*, *generative adverserial networks (GAN)*, *auto encoders*, and *variational auto encoders (VAE)*. |
- Unsupervised learning &mdash;  '&hellip;a type of machine learning in which an algorithm learns patterns and structures in data without any explicit guidance or labeled examples. &hellip;The goal of unsupervised learning is to identify patterns, find underlying structure, and  extract meaningful insights from the data.'  |
- Semi-supervised learning &mdash;  '&hellip;combines elements of supervised and unsupervised learning, using both labeled and unlabeled data to train a model. The labeled data helps guide the learning process, while the unlabeled data aids in discovering patterns and improving generalization&hellip;'  |
- Self-supervised learning &mdash;  '&hellip;is a form of unsupervised learning that creates its own labels from unlabeled data. &hellip;the objective of [the algorithm is] extracting useful information from the data for the task of finding patterns or regularities in the data rather than being explicitly told what to look for.' |
- Reinforcement learning &mdash; The algorithm codifies a form of trial and error &mdash; it '&hellip;involves an agent interacting with an environment and learning to make decisions or take actions in order to maximize rewards or minimize penalties.' |
- Imitation learning &mdash;  '&hellip;is a type of machine learning where the learning algorithm tries to mimic or imitate the behavior of a human expert or some other proficient agent.' |
- Generative AI &mdash; '&hellip;refers to a set of techniques that can generate new content or data that resembles and follows the patterns of existing data. Instead of simply making predictions or classifying data, generative AI models aim to create new information&hellip;' Large language models (LLMs), like generative pre-trained transformers (GPTs), are an example, because they *generate* human-like content only by predicting the next word in a sequence of words based solely on the LLM and the perviously generated words in the stream. |

{% endcomment %}

| AI Learning | Description |
| --- | --- |
| Machine learning | A subset of AI that learns from data so as to identify patterns or make predictions with minimal human intervention. Using automatically built data models, computers can find hidden insights without being explicitly programmed to make predictions on unseen or future data. |
| Supervised learning | '&hellip;is defined by its use of human-labeled datasets to train a model&hellip; to classify data or make predictions accurately. &hellip;The goal of a supervised-learning algorithm is to learn a function that, given an input, predicts the correct output.' |
| Deep learning | A subset of machine learning with algorithms called *artificial neural networks* inspired by the brain. These networks have many layers (hence 'deep'); they are built from *artificial neurons* organized in network architectures; computed with the summation of the (fixed) weighted inputs processed through an activation function; where input features (from new data) are processed into outputs (the predictions). 'There are different types of neural network architectures, including *feed forward networks*, *convolutional networks*, *recurrent neural networks*, *long short-term memory networks (LSTM)*, *generative adverserial networks (GAN)*, *auto encoders*, and *variational auto encoders (VAE)*. |
| Unsupervised learning | '&hellip;a type of machine learning in which an algorithm learns patterns and structures in data without any explicit guidance or labeled examples. &hellip;The goal of unsupervised learning is to identify patterns, find underlying structure, and extract meaningful insights from the data.' |
| Semi-supervised learning | '&hellip;combines elements of supervised and unsupervised learning, using both labeled and unlabeled data to train a model. The labeled data helps guide the learning process, while the unlabeled data aids in discovering patterns and improving generalization&hellip;' |
| Self-supervised learning | '&hellip;is a form of unsupervised learning that creates its own labels from unlabeled data. &hellip;the objective of [the algorithm is] extracting useful information from the data for the task of finding patterns or regularities in the data rather than being explicitly told what to look for.' |
| Reinforcement learning | The algorithm codifies a form of trial and error &mdash; it '&hellip;involves an agent interacting with an environment and learning to make decisions or take actions in order to maximize rewards or minimize penalties.' |
| Imitation learning | '&hellip;is a type of machine learning where the learning algorithm tries to mimic or imitate the behavior of a human expert or some other proficient agent.' |
| Generative AI | '&hellip;refers to a set of techniques that can generate new content or data that resembles and follows the patterns of existing data. Instead of simply making predictions or classifying data, generative AI models aim to create new information&hellip;' Large language models (LLMs), like generative pre-trained transformers (GPTs), are an example, because they *generate* human-like content only by predicting the next word in a sequence of words based solely on the LLM and the perviously generated words in the stream. |

### The technologist's to-do list

- We need smarter, sensitive hands
- We need softer, safer robots
- We need less 'robotic' robots
- We need better ways to build robots
- We need better artificial muscles
- We need more powerful batteries
- We need better sensors
- We need faster brains
- We need to be able to talk naturally to robots

## Responsibility

Chapters 13-17 (*Possible futures*, *What could go wrong?*, *The work of the future*, *Computational education*, *Grand challenges*) describe concerns that humans (the heart) must have when creating AI-driven robots (the chip).

### Possible Futures

Rus argues for the *heart-and-the-chip* possible future, lest we '&hellip;end up with massive, complex systems that we depend on, but don't understand, along with mountains of discarded technologies and electronic waste.' She argues that robots and their attendant models and algorithms must be:

1. Safe &mdash; The obvious requirement that robots are designed with a do-no-harm mentality.
1. Secure &mdash; Guarantee the privacy of personal information with security controls and individual's consent and approval through encryption and strong security practices and strategies.
1. Assistive &mdash; 'The human collaborator should always have the final say when the heart and the chip are working together.'
1. Causal &mdash; Most machine learning is, by its nature, correlative not causal &mdash; causal systems are those that can account for the connection between action and consequence and for internal and external interventions.
1. Generalizable &mdash; Models that are capable of reasoning through the uncertainties that arise when they encounter situations that they have not been trained for.
1. Explainable &mdash; Answering the question, 'why did a model made a decision?' is a goal of [*AI transparency*](https://www.zendesk.com/blog/ai-transparency/) &mdash; including explaining how a systems produces results.
1. Equitable &mdash; Models that avoid widespread algorithmic bias caused by poor representation in training datasets &mdash; the mission of the [Algorithmic Justice League](https://ajl.org/about).
1. Economical &mdash; '&hellip;we absolutely must do everything we can to ensure that these tools aren't merely the playthings of the wealthy elite.'
1. Certified &mdash; Models that are subjected to '&hellip;testing, evaluation, certification, and (perhaps) a regulatory body&hellip; that evaluates the safety and efficacy of intelligent machines and approves them for specific uses&hellip; [which] will shape our creativity, not stifle it.'
1. Sustainable &mdash; Models that are not energy-hungry in their development and deployment (as opposed to those that consume the equivalent of the [lifetime emissions of five cars](https://www.technologyreview.com/2019/06/06/239031/training-a-single-ai-model-can-emit-as-much-carbon-as-five-cars-in-their-lifetimes/) in their creation).
1. Impactful &mdash;'My robotics friends and I are truly trying to develop robots that will make the world a better place. We believe in the use of these machines for the benefit of humanity and the greater good. At the same time, I understand that this attitude will not be universal, and that not every person will invariably work toward building robots to help as many people as possible'

Current machine learning models typically suffer by *not* being causal, explainable, equitable, or sustainable.

### What Could Go Wrong?

Rus suggests including voices and minds from many corners of society and the planet &mdash; technologists, security experts, white hats, policymakers, criminologists, science-fiction writers, ethicists, economists, inventors &mdash; to address the 11 requirements of the heart-and-the-chip [possible future](#possible-futures).

### The work of the future

Chapter 15 makes the assertion that *automation does not automate jobs, it automates tasks*. Rus envisions a future where robots automate tasks in collaboration with humans who provide the reasoning, interaction, and communication. She asks two major questions:

1. How can we adopt and deploy new technologies in such a way that it will help as many people as possible?
1. What can we do now to begin smoothing out the invariable bumpy transition to our new, machine-enabled or -enhanced future?

### Computational education

Chapter 16 discusses the necessity of students *learning* computing and the challenges faced by educators in *teaching* computing. Rus calls *computational thinking* (CT) a top-down approach to problem solving. That means learning CT is more than simply learning programming &mdash; the primary way computing was taught in the last century. Quoting a problem-solving discussion in [StemManifesto](obsidian/Education/StemManifesto.md) about CT:

<blockquote>
Originally described in detail by Jeannette Wing (<a href="https://www.cs.cmu.edu/~15110-s13/Wing06-ct.pdf">2006</a>) and expanded upon by Fred Martin (<a href="https://advocate.csteachers.org/2018/02/17/rethinking-computational-thinking/">2018</a>): '<em>computational thinking is about connecting computing to things in the real world</em>' and '<em>&hellip;is the "connecting tissue" between the world of computer science / programming expertise and the world of disciplinary knowledge.</em>' This connection is a fundamental aspect of STEM problem-solving and what enables,  '<em>&hellip;formulating problems and their solutions so that the solutions are represented in a form that can be effectively carried out by&hellip;</em>' code and computers (<a href="https://www.cs.cmu.edu/~CompThink/resources/TheLinkWing.pdf">2010</a>).
</blockquote>

Rus stresses the creative side of CT so as to, '&hellip;think through complex seemingly impossible tasks.' Again, quoting from [StemManifesto](obsidian/Education/StemManifesto.md):

<blockquote>
Creation is one of the <a href="https://bit.ly/7-big-ideas">7 Big Ideas</a> of computer science: '<a href="https://arc.net/l/quote/btgvyjoh">Computing is a creative human activity&hellip;</a>' (defined as part of the <em><a href="https://web.archive.org/web/20121013163639/http://www.csprinciples.org/home/about-the-project">CS Principles</a></em> project in 2010). <em><a href="https://arc.net/l/quote/xhnxbadg">Creativity</a></em> has its colloquial meaning of 'produce or use original and unusual ideas.' It also means 'the process of creating.' Both important meanings are supported by students generating <em>public products</em> (one of the <a href="https://www.pblworks.org/what-is-pbl/gold-standard-project-design">7 essential elements of PBL</a>) or <em>creating computational artifacts</em> (one of the  <a href="https://k12cs.org/">7 Core Practices</a> of the <em>K-12 Computer Science Frameworks</em>). 
</blockquote>

How does AI fit in?

More [TK](https://en.wikipedia.org/wiki/To_come_(publishing))&hellip;

### Grand challenges

Chapter 17 lists several *grand challenges* to be addressed in a future with more capable and powerful robots: *human health*, *food security*, *energy and electricity*, *sustainability*, *cleaner waters*, *discovery on earth*, *discovery in space*, *truth and democracy*.

# Links

| Link | Description |
| --- | --- |
| [[https://isbn.nu/9781324050230]] | *The Heart and the Chip* |
| [[https://www.csail.mit.edu/person/daniela-rus]] | 'Daniela Rus is the&hellip; Director of the Computer Science and Artificial Intelligence Laboratory (CSAIL) at MIT. Rus’s research interests are in robotics, mobile computing, and data science.'  |
| [[https://www.gregorymone.com/]] | '&hellip;As a ghostwriter, I’ve collaborated with Bill Nye, Susan Cain, Neil deGrasse Tyson, MIT AI Lab Director Daniela Rus, Mattel, and numerous technology executives and thought leaders.' |
| [[https://youtu.be/tCtb0ALFEoY]] | *Daniela Rus & Gregory Mone $\vert$ The Heart and the Chip: Our Bright Future with Robots $\vert$ Talks at Google* (30:00) |

# Image

'I recently received a wonderful present from my students Alexander Amini and Ava Soleimany: my AI-generated portrait in the style of a classical painting. To get this portrait, they trained a model of 5.8 billion images along with their textural descriptions using a probabilistic diffusion model' &mdash; [*The Heart and the Chip*](https://isbn.nu/9781324050230) p. 156

![rus-gen-ai-image-amini-soleymani](obsidian/assets/obsidian/Pasted%20image%2020240828153819.png)

#robotics #ai
<style>h1 { color: rebeccapurple; }</style>