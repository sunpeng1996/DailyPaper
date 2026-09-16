---
title: 'ThinkFlow: Self-Evolving Probabilistic Latent Memory for Lifelong Conversational
  Agents'
title_zh: ThinkFlow：面向终身对话Agent的自进化概率隐式记忆框架
authors:
- Cai Ke
- Xin Liu
- Han Zhang
- Jiangyue Yan
- Zike Yuan
- Ling Deng
- Yue Yu
- Hui Wang
- Ruifeng Xu
affiliations:
- Pengcheng Laboratory
- Harbin Institute of Technology, Shenzhen
- China Unicom Greater Bay Area Innovation Institute
arxiv_id: '2609.17010'
url: https://arxiv.org/abs/2609.17010
pdf_url: https://arxiv.org/pdf/2609.17010
published: '2026-09-15'
collected: '2026-09-16'
category: Agent
direction: 对话Agent · 隐式记忆自进化
tags:
- Conversational Agent
- Latent Memory
- Self-Supervised Learning
- Lifelong Learning
- Personalization
one_liner: 提出端到端隐式记忆框架，绕过显式文本瓶颈实现无标注终身个性化对话
practical_value: '- 可将概率隐式记忆技能(PLMS)设计迁移到用户偏好建模：将多会话行为/对话压缩为解耦隐向量，避免显式画像的信息丢失，适配直播客服、长期个性化推荐等场景

  - 测试时自进化范式可复用：无需人工标注，用用户下一句输入/下一次点击作为自监督信号在线更新记忆，大幅降低个性化系统冷启动成本和标注开销

  - 门控隐式整合器(GLC)的信息增益门可直接用于召回/排序的用户兴趣更新逻辑，自动过滤误点、无效对话等噪声，缓解兴趣漂移问题

  - 上下文超对齐器(CAHA)的低秩适配思路可优化RAG系统的历史上下文与当前查询的分布差，无需全量微调即可实现记忆动态适配，降低推理开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有对话Agent的显式文本记忆系统存在严重信息瓶颈，会丢失用户隐式偏好、情绪变化等细粒度信息，且部署后静态无法自主适配用户习惯，需人工反馈才能更新，难以支撑长期多会话的个性化交互。

### 方法关键点
- 核心设计**概率隐式记忆技能(PLMS)**：将对话流隐藏状态压缩为K个解耦连续隐向量，分别对应事实、情绪、偏好等维度，通过重参数化技巧建模分布不确定性，避免语义干扰
- **门控隐式整合器(GLC)**：通过信息增益门控制新信息写入，过滤冗余问候等噪声，用GRU实现记忆时序更新和优雅遗忘
- **上下文感知超对齐器(CAHA)**：基于当前查询用超网络生成低秩变换矩阵，动态对齐历史隐记忆与当前语义的分布差，作为软提示输入LLM
- 自监督测试时进化范式：第一阶段用全量历史的教师大模型做隐层对齐解决冷启动；第二阶段通过预测用户下一句输入的自监督任务，用预测误差在线更新记忆，实现无标注终身学习

### 关键实验
在MSC、CC、GapChat三个长对话数据集，以及PersonaMem个性化记忆问答基准上测试，对比MemGPT、GraphRAG、Mem0等10+主流记忆系统：基于Qwen3-8B的ThinkFlow在CC数据集Mauve指标达77.20，比最优显式基线高19.01；PersonaMem 1M长上下文下平均准确率41.94，比最优开源基线高3.08；推理速度比显式基线快4~7倍，token消耗仅为显式系统的1/10左右。

### 最值得记住的一句话
放弃显式文本记忆瓶颈，在隐空间通过自监督预测反馈持续进化记忆，是实现长期个性化交互的高性价比路径。
