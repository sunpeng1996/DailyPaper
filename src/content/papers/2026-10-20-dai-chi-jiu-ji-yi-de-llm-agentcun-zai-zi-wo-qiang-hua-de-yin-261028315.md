---
title: 'Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents
  with Persistent Memory'
title_zh: 带持久记忆的LLM Agent存在自我强化的隐私泄露循环
authors:
- Masahiro Kaneko
- Hiromi Arai
- Timothy Baldwin
affiliations:
- MBZUAI
- Third Intelligence
- RIKEN AIP
arxiv_id: '2610.28315'
url: https://arxiv.org/abs/2610.28315
pdf_url: https://arxiv.org/pdf/2610.28315
published: '2026-10-20'
collected: '2026-10-21'
category: Agent
direction: LLM Agent 持久记忆隐私泄露与治理
tags:
- LLM Agent
- Persistent Memory
- Privacy Leakage
- User Profiling
- Mitigation
one_liner: 发现带持久记忆的LLM Agent对话存在自我强化隐私泄露循环，提出低体验损失的干预方案
practical_value: '- 做电商客服、会员专属助手等带记忆的个性化Agent时，可直接给Agent添加系统提示：「除非用户主动提及，否则不得陈述/预设用户的消费能力、地域、年龄等属性」，该方案可将隐私泄露降至无记忆水平，同时保留90%以上的个性化体验增益，效果远优于用户输入过滤、记忆匿名化等方案

  - 做合规的用户建模时，可利用该循环的正向效果：在多轮对话中自然提及已初步推断的用户属性，用户的确认/不纠正行为可大幅提升后续画像的准确率

  - 记忆模块优先采用RAG检索模式而非全量历史上下文灌入，可降低15%-20%的隐私泄露量，因为每次对话仅用到少量相关历史信息'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前商用LLM Agent普遍采用持久记忆实现跨会话个性化，免去用户重复输入信息，但记忆中存储的用户隐私属性一旦泄露将带来极高风险。现有研究大多将对话记录视为静态数据分析泄露风险，未关注记忆本身会改变用户后续对话行为、进一步放大泄露的动态过程，且无低损的落地干预方案。
### 方法关键点
- 用Claude Sonnet 5模拟具备24项真实人口属性（年龄、收入、职业、家庭情况等，来自美国人口普查微数据）的用户，与4种不同的支持Agent（GPT-5.6 Luna/Terra、Qwen3.8-27B、DeepSeek V4-Flash）进行最多80轮多会话交互，控制相同的用户请求序列，隔离记忆对对话的影响。
- 定义empirical leakage为从完整对话记录中可正确推断的用户属性占比，拆分「记忆信息→Agent响应预设属性→用户确认/不纠正→写入记忆」的闭环链路。
- 横向对比三类干预方案：用户输入过滤、记忆写入时匿名化、Agent响应侧指令约束。
### 关键结果
- 开启记忆后，Agent响应质量（helpfulness+coherence）提升30%~40%，但隐私泄露率比无记忆组高10%~15%，且差距随会话数持续扩大。
- 最优干预为响应侧指令约束：仅要求Agent不主动陈述/预设用户属性，即可将泄露率降至无记忆水平，同时保留95%的helpfulness增益和93%的coherence增益，远优于用户侧/记忆侧过滤方案（后两者会损失60%以上的个性化增益）。
- 移除Agent对属性的提及，后续泄露的降低幅度是单轮效果预测的2倍，验证了循环的自我强化特性。
### 最值得记住的一句话
带持久记忆的LLM Agent的隐私泄露风险不是静态的，而是会通过「Agent预设属性→用户默认确认→写入记忆」的循环不断放大，最有效且低成本的干预点是Agent的响应生成环节，而非用户输入或记忆存储环节
