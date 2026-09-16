---
title: Interactive Memory Learning for Long-Term Conversations
title_zh: 面向长期对话的交互式记忆学习框架ICML
authors:
- Cai Ke
- Jiangyue Yan
- Han Zhang
- Xin Liu
- Zike Yuan
- Yue Yu
- Hui Wang
- Ruifeng Xu
affiliations:
- Harbin Institute of Technology, Shenzhen
- Pengcheng Laboratory
arxiv_id: '2609.17088'
url: https://arxiv.org/abs/2609.17088
pdf_url: https://arxiv.org/pdf/2609.17088
published: '2026-09-15'
collected: '2026-09-16'
category: Agent
direction: Agent 长期对话记忆自进化优化
tags:
- LLM Agent
- Memory Management
- Reinforcement Learning
- Multi-Agent
- Long-term Conversation
one_liner: 提出多Agent协同的ICML框架，通过在线RL与延迟奖励实现记忆策略自进化适配长期对话需求
practical_value: '- 电商导购/智能客服场景可直接复用Planner+Trigger双Agent记忆架构：Planner负责筛选用户高价值稳定偏好（如饮食忌口、消费预算、风格偏好）过滤噪声，Trigger负责动态召回匹配当前请求的记忆，比静态全量记忆存储+向量检索的方案准确率更高、成本更低

  - 跨会话延迟奖励机制可解决用户偏好更新冲突问题：当用户新需求与旧记忆冲突时，将后续响应的正/负反馈回溯到历史记忆存储/更新决策，让记忆策略自动适配用户最新偏好，避免出现“之前说吃素现在推荐肉”的错误

  - 回溯会话合成方案可快速冷启动新用户记忆策略：针对新用户的少量初始交互，反向生成逻辑自洽的历史偏好会话链，标注后做预热训练，不用从零开始探索，大幅提升新用户前几轮交互的体验

  - 双Agent能力对齐可降低落地成本：实验证明Planner和Trigger的模型规模匹配时性价比最高，不需要两个都用大模型，小参数对齐的双Agent效果甚至优于参数错配的大模型组合，适合业务场景平衡效果和算力成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长期对话Agent的记忆机制多为静态启发式范式，被动归档全量交互信息，没有自适应的记忆价值评估能力，无法随用户需求变化自进化，容易出现旧偏好与新需求冲突的问题，同时存在记忆冷启动难、奖励稀疏、长上下文成本高的痛点，难以支撑长期个性化交互。

### 方法关键点
- 设计回溯会话合成pipeline：以用户初始种子会话为基础，反向生成逻辑一致的历史会话链，正向标注记忆存储/召回标签，生成高质量专家数据做冷启动预热，解决新用户初始交互无有效记忆的冷启动问题
- 双Agent协同架构：Planner Agent作为记忆守门员，判断当前交互信息是否值得存储，过滤低价值噪声；Trigger Agent根据当前查询动态召回匹配的记忆片段，支撑响应生成
- 跨会话真值奖励机制：记忆被Trigger成功调用并获得正反馈后，把奖励回溯到Planner的历史存储决策，用PPO算法联合优化两个Agent的策略，实现协同进化

### 关键实验
在CC、MSC、GC三个真实长期对话数据集上测试，对比长上下文LLM、Mem0、MemoryOS、MemoryBank等7个SOTA基线，基于Qwen3-8B的ICML在CC数据集上Mauve得分达80.33，比次优基线高4.91；检索延迟仅13ms，比基线低85%以上；交互10轮后Planner精度、Trigger召回率持续提升，无性能衰减。

**最值得记住的一句话**：对于长期交互场景，主动学习「什么值得记、什么时候该调用」，远比被动存储全量历史信息的效果和效率更优。
