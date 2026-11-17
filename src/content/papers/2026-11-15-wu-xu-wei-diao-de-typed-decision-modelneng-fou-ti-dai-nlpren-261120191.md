---
title: Do We Still Need Fine-Tuned Classifiers? Swapping Typed Decision Models into
  24 ACL-Venue Papers
title_zh: 无需微调的Typed Decision Model能否替代NLP任务微调分类器？
authors:
- Marek Šuppa
- Jaroslav Kopčan
affiliations:
- Comenius University in Bratislava
- Cisco Systems
- Kempelen Institute of Intelligent Technologies
arxiv_id: '2611.20191'
url: https://arxiv.org/abs/2611.20191
pdf_url: https://arxiv.org/pdf/2611.20191
published: '2026-11-15'
collected: '2026-11-17'
category: LLM
direction: 大模型分类方案 · 零/少样本分类
tags:
- Typed Decision Model
- Zero-Shot Classification
- Few-Shot Learning
- Fine-Tuning
- LLM Evaluation
one_liner: 在24篇ACL论文的46个测试集上验证Typed Decision Model替代微调分类器的边界
practical_value: '- 电商/推荐场景的低资源分类任务（用户评论情感识别、query意图分类、短文本合规校验）可优先用Typed Decision
  Model（TDM）跑零-shot基线，成本仅$0.05/千条，达标即可直接上线，省掉微调算力与标注成本

  - 零-shot效果不足时，仅需500条标注+GEPA风格prompt优化+小逻辑回归校准，即可填平72%与微调方案的性能差，全程无需自有GPU，单任务优化成本中位数$1.66，适配快速迭代的小流量业务

  - 大标签空间场景（如百万级商品类目分类）或对准确率要求极高的场景，优先选择LoRA微调开源大模型，仅需500条标注即可填平97%的性能差，效果比TDM方案更稳定

  - 优化分类prompt时优先补全标签名未写明的标注隐含约定，可直接提升约2.5个点的准确率，投入产出比远高于盲目调整prompt结构'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前NLP分类任务普遍依赖任务专属微调分类器，prompt大模型零-shot效果普遍落后于微调方案，而新出现的Typed Decision Model（TDM，也叫System 1模型）可直接输出分类概率无需训练，但缺乏对其替代微调分类器的能力与边界的系统性验证。

### 方法关键点
- 选取2024-2026年ACL/EMNLP/NAACL/EACL的24篇论文，替换其核心预测器为TypeSafe的Jev TDM，保留原论文的数据集划分、标签定义、评估指标，构建包含46个英文测试集的TDM-Gauntlet基准。
- 分三层测试TDM效果：零-shot仅基于原论文标签定义写prompt；加校准（400条标注拟合类别偏置/温度）；加GEPA风格prompt优化（500条标注+验证集搜索最优prompt，结果作为特征喂给小逻辑回归）。
- 对比基线包括原论文微调分类器、同标注量微调的RoBERTa/DeBERTa编码器、同标注量LoRA微调的Qwen3.8-27B大模型。

### 关键结果
- 零-shot下Jev直接在12/46测试集上达到或超过原论文微调方案效果，多为标签语义清晰的二分类/小标签空间任务，推理成本仅$0.05/千条样本。
- 零-shot效果不足的场景中，18/34的性能差来自标签名未包含的标注隐含约定，补全约定可直接提升2.5个点准确率。
- 500条标注加prompt优化可填平72%与原微调方案的性能差，效果与同标注量微调编码器相当（后者填平59%）；同标注量下LoRA微调Qwen3.8-27B可填平97%的性能差。

> 最值得记住的一句话：分类任务可先试零-shot TDM快速验证，效果不足用小批量标注做prompt优化，仅大标签空间或极致准确率要求才需要微调
