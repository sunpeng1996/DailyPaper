---
title: Read the Room Before Your Model Generates
title_zh: 基于场景感知的大语言模型动态采样温度自适应选择框架
authors:
- Muyao Kong
- Zhihao Lin
affiliations:
- New York University
- Independent Researcher
arxiv_id: '2610.18820'
url: https://arxiv.org/abs/2610.18820
pdf_url: https://arxiv.org/pdf/2610.18820
published: '2026-10-13'
collected: '2026-10-15'
category: LLM
direction: LLM解码优化 · 场景感知
tags:
- Temperature_Sampling
- Scenario_Aware
- LLM_Decoding
- Transformer_Hidden_State
- Adaptive_Generation
one_liner: 从Transformer中间层隐状态提取场景嵌入，动态匹配最优采样温度提升交互生成性能
practical_value: '- 可复用「从Transformer中间层而非输出层提取语义/场景特征」的思路，适配电商客服、导购Agent的回复风格：售后咨询等严谨场景用低温度，种草闲聊等开放场景用高温度，提升用户体验

  - 场景轴定义+余弦相似度加权插值的范式可迁移到搜索推荐的意图适配：将用户query映射到不同意图轴，动态调整召回排序的策略权重，提升匹配精度

  - 工程上仅需新增少量参数训练Scenarize模块，推理延迟比贪心解码仅高2.5%，可快速上线到现有LLM交互系统'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM采样温度多采用全局固定设置或基于token熵、上下文做简单校准，未考虑交互场景的本质差异：不同场景（如严谨问答/脑暴/闲聊）对生成内容的严谨性、创造性要求差异极大，实验显示固定温度调整会导致16%~17%的交互目标结果翻转，严重影响生成效果。
### 方法关键点
- Scenario-Actor框架主干LLM完全冻结，仅新增极少量参数，分为Scenarize和Actout两个模块
- Scenarize模块取Transformer中间层（Llama-3.1为第16层）隐状态作为输入，用轻量RNN逐token更新场景嵌入，通过三元组损失训练，保证相似场景嵌入距离近、相反场景距离远
- Actout模块基于心理学DIAMONDS场景分类定义5个场景轴，通过场景嵌入与各轴的余弦相似度加权插值，得到适配当前场景的采样温度
### 关键结果
基于Llama-3.1-8B-Instruct测试，对比固定温度、nucleus采样、EDT等基线：AgentSense社交交互场景目标完成率达0.8015，比最优固定温度基线高2.14个百分点；AlpacaEval长度控制胜率达30.03%，比最优基线高4.35个百分点；MT-Bench得分7.91，优于多数自适应解码方法；推理延迟仅比贪心解码高2.5%，几乎无额外性能损耗。
最值得记住的结论：Transformer中间层隐状态包含比最终输出层更丰富的场景语义信息，更适合做细粒度的生成策略适配。
