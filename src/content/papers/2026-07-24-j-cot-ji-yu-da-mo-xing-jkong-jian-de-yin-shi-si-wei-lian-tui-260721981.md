---
title: 'J-CoT: Chain-of-Thought in J-Space'
title_zh: J-CoT：基于大模型J空间的隐式思维链推理框架
authors:
- Junde Wu
- Jiayuan Zhu
- Fengling Liu
- Minhao Hu
- Jiazhen Pan
affiliations:
- University of Oxford
- Imprint Lab
- Stanford University
arxiv_id: '2607.21981'
url: https://arxiv.org/abs/2607.21981
pdf_url: https://arxiv.org/pdf/2607.21981
published: '2026-07-24'
collected: '2026-07-27'
category: Reasoning
direction: 大模型隐式推理 · 思维链优化
tags:
- Chain-of-Thought
- J-space
- Latent Reasoning
- LLM Inference
- Recurrent Reasoning
one_liner: 提出基于词汇索引J空间的隐式思维链框架，兼顾推理灵活性与信息选择性
practical_value: '- 电商/广告Agent的推理模块优化可复用J-CoT轻量中间状态机制，替代全隐状态回传或显式CoT，降低推理时延的同时保留关键决策信息

  - 生成式推荐/个性化文案生成场景可借鉴多carrier设计，用多通道J-thought并行保留用户偏好、商品属性、活动规则等中间特征，避免生成时信息丢失

  - 推理框架工程实现可复用其自适应停止策略：监控连续两次中间状态的变化率，动态调整推理步数，平衡效果与算力成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统显式CoT需要将中间推理步骤序列化为自然语言，浪费模型容量在语法、话术生成上，还会强制未成熟的推理过程提前绑定到具体语义；而全隐式推理直接传递完整隐状态，缺乏对下一步所需信息的选择机制，容易引入无关噪声，两种方案都存在效率与效果的瓶颈。
### 方法关键点
- 基于大模型原生J空间（词汇索引的跨层隐层坐标系统）定义J-thought作为推理循环的中间状态，无需解码为自然语言也无需传递全量隐向量，仅传递词汇维度的非负系数
- 设计多个非语言占位符（carrier）作为J-thought的读写载体，推理周期内carrier参与正常Transformer计算，仅在周期边界读写J空间系数
- 提供两种落地配置：J-CoT-Zero无需额外训练，直接适配预训练模型；J-CoT-Train仅优化carrier嵌入和读入门控，主干模型完全冻结，训练成本极低
- 内置自适应停止策略，监控连续两次J-thought的变化率，低于阈值即终止推理，避免无效计算
### 关键结果
基于Qwen3-8B等多尺寸主干，在GSM8K、MATH-500、HumanEval+等8个数学、科学、代码推理数据集上测试：J-CoT-Zero零额外训练就比最强隐式推理基线SIM-Coconut平均高0.4个点，比显式CoT高2.1个点；J-CoT-Train仅优化极少量参数，平均精度达50.2，比SIM-Coconut高2.7个点，且性能随模型尺寸、推理步数正向缩放。
> 最值得记住：介于全显式语言和全隐式向量之间的词汇锚定半结构化中间状态，是兼顾推理灵活性与效率的最优解之一
