---
title: Understanding MoE Decisions Beyond Gradients
title_zh: 超越梯度的MoE大模型决策机制解释方法
authors:
- Zhen Xu
- Zitao Zhang
- Kevin Zhao
- Xuefeng Liu
affiliations:
- University of Chicago
- eBay
- University of Florida
arxiv_id: '2611.26075'
url: https://arxiv.org/abs/2611.26075
pdf_url: https://arxiv.org/pdf/2611.26075
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: 大模型可解释 · MoE决策归因
tags:
- MoE
- Interpretability
- Gradient Attribution
- Model Debugging
- Causal Intervention
one_liner: 新增下游专家切换效应修正项，大幅提升MoE干预效果预测精度
practical_value: '- 电商/广告场景部署MoE推荐/生成服务时，可复用该方法定位影响输出的关键专家，快速排查badcase根因，避免盲调模型参数

  - 迭代MoE路由模块时，可通过「固定下游专家选择」的对照实验，量化路由切换对最终输出的影响占比，指导路由策略优化

  - 搭建MoE可解释性工具时，不能完全依赖梯度基归因方法，需补充路由切换的效应估计模块，避免漏判关键影响组件'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
梯度基的模型干预效果归因在MoE场景存在严重缺陷：替换某层专家会触发后续层的专家选择切换，这种离散跳变无法被局部导数捕捉，导致预测干预对输出得分的影响误差极高，无法准确定位MoE中影响决策的关键组件。

### 方法关键点
- 基于二阶梯度估计（HVP1），新增下游专家切换效应修正项：对比「允许下游重选专家」和「固定下游原有专家」两种响应模型的输出差，估计路由切换带来的额外效应，最终预测值为梯度估计加修正项
- 响应模型基于单次前向的专家输出、路由得分和导数构建，可复用同一prompt下的多干预预测，无需拟合实测干预结果

### 关键实验
在Qwen3.6-35B、Gemma4-26B两款MoE模型，MMLU-Pro、SuperGPQA、HLE三个问答数据集上测试，对比一阶AtP、多步二阶HVP5基线：
1. 预测答案得分变化的MAE相对HVP5最多降低63%，Qwen3.6上平均降60%，Gemma4上平均降47%
2. 定位Top5影响最大的专家组合的Recall@5从HVP5的63.3%提升至79.2%（Qwen3.6），从78.3%提升至83.3%（Gemma4）
3. 固定下游专家选择后HVP5的误差几乎消失，验证梯度基方法的误差核心来自路由切换

**最值得记住的一句话**：MoE干预效应的误差有60%以上来自下游专家切换的离散跳变，仅靠增加梯度采样步数无法消除，必须显式建模路由变化的影响。
