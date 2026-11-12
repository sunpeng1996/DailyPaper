---
title: Incentivizing Self-Learning in Large Language Models via Reinforcement Learning
title_zh: 基于强化学习激励大语言模型自主学习能力
authors:
- Lingkai Kong
- Yuzhe Gu
- Haiteng Zhao
- Zijian Wu
- Youqing Fang
- Zhouqi Hua
- Yanan Sun
- Kai Chen
- Wenwei Zhang
affiliations:
- Shanghai AI Laboratory
- Shanghai Jiao Tong University
- MMLab, The Chinese University of Hong Kong
- University of Science and Technology of China
- Fudan University
arxiv_id: '2610.39671'
url: https://arxiv.org/abs/2610.39671
pdf_url: https://arxiv.org/pdf/2610.39671
published: '2026-10-28'
collected: '2026-11-12'
category: Agent
direction: Agent 自主学习能力优化
tags:
- RL
- Self-Learning
- Retrieval Agent
- Long Context
- GRPO
one_liner: 设计细粒度强化学习框架激励LLM自主检索长文本参考资料，提升复杂任务跨域泛化能力
practical_value: '- 搜索推荐/电商导购Agent的奖励设计可复用本方法的三层RL奖励逻辑：最终业务目标奖励+探索bonus+中间工具调用信用分配，既鼓励Agent主动检索商品参数、平台规则、活动政策等知识库，又避免无效工具调用，提升复杂导购、咨询场景的解决率

  - 长文本参考资料的交互接口设计可直接复用：先取目录→关键词搜索→读对应章节的三层检索逻辑，适配电商大篇幅商品说明、平台规则、售后政策等长文档的自主查询场景，减少无效上下文占用KV
  cache

  - GRPO训练时加入退火探索bonus的trick可直接迁移：解决训练后期Agent能力变强后不愿意调用外部工具的问题，大幅提升跨新类目、新活动规则的OOD场景泛化能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM依赖参数知识或RAG解决知识密集型任务，但陌生领域任务需要知识获取与推理深度耦合，单纯召回聚合或预拼接上下文无法满足需求，LLM边执行任务边自主检索、学习、应用长文本参考资料的自主学习能力训练方法存在空白。
### 方法关键点
- 构建教材式数学解题任务：从158本高等数学教材提取5183道证明题，隐藏习题答案，仅保留定义、定理等参考内容，要求模型自主检索学习相关知识完成证明
- 设计BookNavigator交互接口：支持获取目录、关键词搜索、读取指定章节三类操作，模拟人类查阅教材的学习流程
- 优化RL奖励机制：基于GRPO算法，加入退火探索bonus（鼓励主动调用工具）+ 轮次级工具信用分配（区分有用/无用检索，避免无效调用），用LLM-as-judge评估最终证明正确性作为核心奖励
### 关键实验结果
基于Intern-S2-Preview-35B训练，对比无教材、固定召回等基线：
- 域内/跨教材/跨学科数学证明整体准确率从51.5%提升至79.5%，超出最强固定召回基线6.4个百分点
- 跨任务泛化效果显著：BrowseComp-Plus benchmark提升1.7个百分点，CL-bench提升2.3个百分点
### 核心结论
RL不仅能优化特定任务执行效果，还能训练出领域无关的自主学习策略，让LLM学会如何学习，而非仅记忆特定领域知识
