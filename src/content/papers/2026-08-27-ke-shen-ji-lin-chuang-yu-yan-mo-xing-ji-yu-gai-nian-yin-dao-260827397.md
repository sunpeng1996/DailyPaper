---
title: 'Making Clinical Language Models Auditable: Concept-Guided Fine-Tuning for
  Robust Prediction'
title_zh: 可审计临床语言模型：基于概念引导微调的鲁棒预测方法
authors:
- Jin Mu
- Guanhua Chen
affiliations:
- University of Wisconsin–Madison
arxiv_id: '2608.27397'
url: https://arxiv.org/abs/2608.27397
pdf_url: https://arxiv.org/pdf/2608.27397
published: '2026-08-27'
collected: '2026-08-30'
category: Training
direction: 大语言模型可解释微调与鲁棒性优化
tags:
- SAE
- Fine-tuning
- LLM Interpretability
- Out-of-distribution Robustness
- Auditable AI
one_liner: 提出基于SAE的CAST微调框架，抑制临床文本artifact提升鲁棒性同时提供预测审计轨迹
practical_value: '- SAE提取Transformer中间激活稀疏可解释特征的方法，可迁移到LLM4Rec、排序模型的黑盒归因分析，定位模型依赖的噪声特征（如电商文案模板、评论套话等artifact）

  - LLM辅助标注隐层特征+业务先验约束（可替换为电商类目、用户标签体系）的方法，可快速识别模型学习到的伪相关shortcut，提升分布外泛化能力

  - 微调阶段通过残差减法抑制已识别artifact隐层特征的trick，无需改动模型结构，可直接复用到生成式推荐、搜索Query改写模型的微调流程'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
临床LLM在院内分布数据上精度优异，但部署到分布外场景性能暴跌，核心原因是模型学习到笔记模板、分隔符、固定套话等和患者状态无关的数据集特有artifact shortcut，且决策过程不可审计，无法满足高风险场景合规要求。
### 方法关键点
CAST框架基于SAE实现：1）用Sparse Autoencoder从Transformer中间层激活提取稀疏、人类可解释的特征；2）通过LLM辅助标注流水线+ICD-10检索约束，为SAE隐层特征打标签，识别artifact相关隐变量；3）微调阶段通过残差减法抑制已验证的artifact隐变量，同时输出每个预测对应的概念级归因路径用于审计。
### 关键结果
在MIMIC-IV出院笔记死亡率预测任务上，CAST精度优于对应微调编码器基线，性能与强LLM基线持平，同时可输出预测依赖的临床概念、训练阶段抑制的artifact概念的特征级审计轨迹。
