---
title: What Survives Distillation? A Mechanistic Interpretability Study of GPT-2 and
  DistilGPT-2
title_zh: 蒸馏后哪些能力保留了？GPT-2与DistilGPT-2的机制可解释性研究
authors:
- Nabeelah Faumi
- Deshan Sumanathilaka
affiliations:
- Informatics Institute of Technology, Sri Lanka
arxiv_id: '2610.37157'
url: https://arxiv.org/abs/2610.37157
pdf_url: https://arxiv.org/pdf/2610.37157
published: '2026-10-27'
collected: '2026-10-28'
category: LLM
direction: 大模型知识蒸馏 · 机制可解释性
tags:
- Knowledge Distillation
- Mechanistic Interpretability
- GPT-2
- DistilGPT-2
- Model Compression
one_liner: 通过机制可解释性方法发现知识蒸馏存在压缩-崩溃二分特性，整体指标无法反映电路完整性
practical_value: '- 电商/推荐场景做LLM蒸馏落地（如文案生成、Query理解小模型）时，不能只看PPL、准确率等整体指标，要针对业务核心依赖的推理能力（如属性判断、指代消解）做专项评测，避免整体指标达标但核心能力隐性崩溃导致线上故障

  - 若业务用蒸馏小模型做推理任务（如价格比较类Query识别、订单语义理解），可参考文中激活补丁、注意力模式匹配方法，定位小模型是否完整保留对应功能的电路，针对性优化蒸馏目标

  - 深度减半类蒸馏会将教师模型的深层能力压缩到学生模型的比例对应层，做小模型LoRA微调时可优先针对对应比例层训练，效率更高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
知识蒸馏是LLM落地的核心压缩手段，但传统蒸馏仅关注PPL等整体指标，无法判断蒸馏后模型底层推理电路的完整性，深度减半类蒸馏对依赖深层计算的能力的影响尚未被明确量化，业务场景下核心能力的隐性崩溃会带来不可控的线上风险，亟需明确蒸馏对不同推理电路的影响规律。

### 方法关键点
- 选取12层GPT-2为教师、6层DistilGPT-2为学生，针对两个经因果验证的经典推理电路：多阶段指代消解IOI电路、数值比较GT电路做对比分析
- 用线性CKA、logit lens、注意力模式分解、稀疏自编码器特征统计、激活补丁等工具，从表征相似度、电路功能两个维度做全链路评估
- 设计两种层匹配规则：同索引匹配、比例匹配（学生层d对应教师层⌊d·11/5⌉），规避层结构差异带来的评估偏差

### 关键实验结果
数据集采用TinyStories验证集、WikiText-2测试集，IOI任务上DistilGPT-2准确率仅35.2%（教师为94.8%），电路完全崩溃甚至出现结果反向；GT任务上DistilGPT-2恢复87.7%的教师性能，教师层9的比较头被重映射到学生层4，注意力模式Pearson r达0.945；比例匹配下整体表征相似度CKA均值达0.921，同索引匹配仅0.752，验证学生是压缩而非截断教师的表征路径。

### 核心结论
知识蒸馏存在压缩-崩溃二分特性，仅依赖PPL等整体指标无法判断模型核心推理能力的完整性，电路压缩兼容性决定了蒸馏后的能力留存情况
