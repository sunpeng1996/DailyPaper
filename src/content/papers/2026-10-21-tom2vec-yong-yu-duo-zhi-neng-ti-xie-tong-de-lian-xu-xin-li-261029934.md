---
title: 'ToM2Vec: Continuous Theory-of-Mind Tokens for Multi-Agent Coordination'
title_zh: ToM2Vec：用于多智能体协同的连续心理理论嵌入表示
authors:
- Nithin Sivakumaran
- Ali Payani
- Hyunji Lee
- Mohit Bansal
- Elias Stengel-Eskin
affiliations:
- UNC Chapel Hill
- Cisco
- The University of Texas at Austin
arxiv_id: '2610.29934'
url: https://arxiv.org/abs/2610.29934
pdf_url: https://arxiv.org/pdf/2610.29934
published: '2026-10-21'
collected: '2026-10-22'
category: MultiAgent
direction: 多智能体协同 · 心理理论建模
tags:
- ToM
- Multi-Agent
- Latent Reasoning
- LLM Agent
- Self-Play
one_liner: 通过自监督学习连续隐层心理理论令牌，提升多智能体协同性能且可泛化到未知搭档模型
practical_value: '- 多智能体协同场景（如电商客服多Agent联动、广告投放策略多Agent博弈）可复用ToM2Vec的隐层令牌建模思路，避免显式输出搭档推理文本导致的单路径假设偏差

  - 自监督训练范式可迁移：用自玩场景中搭档的真实推理隐层状态做监督信号，仅用余弦相似度损失训练，不需要额外标注，适合业务端低成本优化Agent协同能力

  - 跨模型泛化结论可复用：用开源小模型训练的ToM能力可直接迁移到闭源大模型搭档，业务场景可先在小模型上验证方案再对接生产级大模型，降低试错成本

  - 推荐系统用户意图预判、直播电商观众购买意愿推断等用户心理建模场景，可参考该思路将用户潜在意图编码为连续隐层令牌，替代显式意图分类，覆盖多可能性意图'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM智能体做多智能体协同时，用文本做心理理论（ToM）建模容易固定为单一路径假设，无法覆盖搭档的多种潜在意图，导致协同冲突、效率低下，而显式提示ToM的效果增益非常有限。

### 方法关键点
- 训练阶段采用自玩范式，将搭档的推理文本分段后提取对应隐层状态，构造K个连续ToM令牌作为监督目标
- 主模型仅用余弦相似度损失，学习从自身观测上下文预测匹配的连续ToM令牌，无额外任务奖励优化
- 推理阶段主模型先生成K个ToM令牌作为上下文前缀，再输出自身推理和动作，不需要访问搭档的私有信息

### 关键实验
在Overcooked-AI、多轮协商、Decrypto、Hanabi等5类覆盖协作、竞争、混合动机的多智能体场景验证，对比未训练LLM、提示式ToM、显式文本ToM训练等7种基线方法；核心结果：Overcooked平均得分较基线提升12分，协商成功率从62%提升到71%，跨模型测试时对接训练中未见过的GPT-5.4搭档仍能平均提升17.3分。

### 核心结论
用连续隐层令牌做心理理论建模的效果远好于显式文本ToM，且具备跨模型泛化能力
