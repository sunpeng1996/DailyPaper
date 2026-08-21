---
title: Improved Confidence Estimates for Black-Box Large Language Models
title_zh: 面向黑盒大语言模型的置信度估计优化方法
authors:
- Sokhna Diarra Mbacke
- Mouloud Belbahri
- Gabriel Loaiza-Ganem
affiliations:
- Layer 6 AI
- TD Insurance
arxiv_id: '2608.19323'
url: https://arxiv.org/abs/2608.19323
pdf_url: https://arxiv.org/pdf/2608.19323
published: '2026-08-19'
collected: '2026-08-21'
category: LLM
direction: 大语言模型 · 不确定性量化（UQ）
tags:
- Uncertainty Quantification
- Black-box LLM
- Confidence Estimation
- Calibration
- Supervised Learning
one_liner: 利用已有UQ得分与相似查询历史特征训练轻量分类器，优化黑盒LLM置信度估计
practical_value: '- 电商客服Agent、生成式推荐文案生成场景可直接复用框架：将现有hallucination检测得分、语义一致性得分、verbalized
  confidence作为基础特征，叠加历史相似query的LLM回答正确率统计特征，训练轻量分类器判断输出可靠性，低置信度输出自动触发RAG召回或人工审核，新增计算开销可忽略

  - 算力受限的高吞吐场景可选择低成本配置：仅保留verbalized confidence与邻域特征，无需多次采样生成多轮回复，即可比原生Ptrue提升5%~8%的正确性识别AUROC，满足线上低延迟要求

  - 参考k-DPP采样策略构建参考数据集，在相同标注数据规模下提升邻域特征的覆盖度与有效性，缓解冷启动阶段参考样本不足的问题'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有黑盒LLM的不确定性量化（UQ）方法多为零-shot启发式方案：自报告verbalized confidence普遍存在过置信问题，多采样生成的语义不确定性得分无法直接作为校准概率用于下游决策。而工业场景部署LLM前必然会积累标注的效果评估数据集，这一核心资源此前未被用于UQ优化，导致置信度估计的准确率和校准度均无法满足高风险场景（如电商客服应答、营销文案正确性校验）的要求。
### 方法关键点
- 复用现有UQ得分作为基础特征，不额外设计新的UQ计算逻辑，可兼容任意黑盒LLM与现有UQ方案
- 拆分标注数据集为训练集与参考集，对每个query检索参考集中k=20个最相似样本，提取邻域内回答正确率的均值/标准差、样本相似度的均值/标准差等统计特征，补充单query UQ得分缺失的历史经验信息
- 拼接两类特征后训练轻量分类器（L1正则逻辑回归、随机森林）预测回答正确性，最后通过温度缩放优化校准度，整体训练与推理开销远低于LLM生成成本
### 关键实验
在CS_QA、NQ、SciQ、SimpleQA四个公开基准上测试GPT4.1全系列、LLaMA4 Maverick模型，对比Ptrue、温度缩放Ptrue、APRICOT、语义UQ等基线：AUROC平均比最优基线高2.7%~15%，ECE平均比原生Ptrue降低80%以上；仅用Ptrue加邻域特征的低成本版本也可稳定优于原生Ptrue，无需额外多轮生成开销。
### 核心结论
LLM置信度估计本质是监督学习问题，任何现有UQ得分都可作为特征结合场景标注数据进一步优化，而非直接作为最终置信度使用
