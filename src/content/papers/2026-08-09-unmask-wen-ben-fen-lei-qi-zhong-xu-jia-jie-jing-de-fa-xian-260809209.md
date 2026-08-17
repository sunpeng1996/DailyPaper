---
title: 'UNMASK: Discovering and Causally Verifying Spurious Shortcuts in Text Classifiers'
title_zh: UNMASK：文本分类器中虚假捷径的发现与因果验证
authors:
- Chidaksh Ravuru
- Shashank Srivastava
affiliations:
- University of North Carolina, Chapel Hill
arxiv_id: '2608.09209'
url: https://arxiv.org/abs/2608.09209
pdf_url: https://arxiv.org/pdf/2608.09209
published: '2026-08-09'
collected: '2026-08-17'
category: LLM
direction: LLM鲁棒性 · 虚假关联因果验证
tags:
- Spurious Correlation
- Causal Verification
- Text Classification
- OOD Generalization
- Robustness
one_liner: 无需额外人工标注的全自动pipeline，可发现、因果验证并缓解文本分类器的虚假关联
practical_value: '- 可迁移到电商评论情感分类、query意图识别等文本分类场景，自动发现训练数据虚假关联，降低OOD样本误判率

  - 无人工标注的因果验证流程可复用在推荐排序模型的特征置信度校验，避免引入与目标无因果关系的伪特征

  - 无需人工标注分组的DFR改进方案，可直接复用在LLM微调、Reward Model训练的去偏流程，降低标注成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
基于众包语料训练的文本分类模型常利用与标签关联但无因果关系的表层虚假模式，基准性能高但OOD/对抗样本表现差；现有方案需人工定义特征词表或仅能部分自动化发现，无法桥接数据集相关性与模型依赖的缺口。
### 方法关键点
UNMASK全自动无标注pipeline流程：1）生成布尔表达式形式的候选表层模式；2）经独立复制的统计协议过滤；3）通过反事实干预确认特征与模型预测的因果依赖；4）因果验证特征作为无标注分组输入Deep Feature Reweighting，省去标准DFR所需的人工组标注。
### 关键结果
在MNLI训练的BERT/RoBERTa上分别验证9/10、6/10已知偏差特征，HANS精度最高提升12.58pp；CivilComments-WILDS数据集上无需人口标注即可达到手动标注DFR的70.1%最差组精度；可泛化到Reward Model偏好数据，挖掘RewardBench2可解释虚假关联。
