---
title: 'CondUQ: Calibrated Conditional Uncertainty Quantification Using Distribution
  Matching'
title_zh: CondUQ：基于分布匹配的校准条件不确定性量化方法
authors:
- Shizhuang Wang
- Tianhao Wang
- Xingqun Zhan
affiliations:
- Shanghai Jiao Tong University
- Nanyang Technological University
arxiv_id: '2611.33939'
url: https://arxiv.org/abs/2611.33939
pdf_url: https://arxiv.org/pdf/2611.33939
published: '2026-11-25'
collected: '2026-11-27'
category: Training
direction: 模型训练 · 不确定性量化校准
tags:
- Uncertainty Quantification
- Distribution Matching
- Conditional Modeling
- Black-box Calibration
- Unsupervised Learning
one_liner: 提出无需修改原模型的黑盒条件不确定性量化方法condUQ，通过分布匹配拟合随观测因素变化的误差分布
practical_value: '- 推荐/广告排序模型置信度校准可复用condUQ外挂思路：无需改动原有排序模型，基于输入特征、模型中间隐层输出等可观测因素拟合不同场景下的预测误差分布，提升排序结果可靠性

  - 生成式推荐/LLM Agent推理结果不确定性评估可借鉴无监督QI训练方法：无需人工标注质量标签，通过分布匹配目标端到端训练QI预测器，自动区分不同输入对应的输出置信度

  - 多场景流量分发可基于condUQ输出的不确定性分层：对预测误差大的低置信度结果增加探索流量，高置信度结果优先保障收益，平衡推荐效果与稳定性'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有不确定性量化方案多为无条件形式，无法捕捉模型误差随输入质量、运行条件等因素的动态变化，单一高斯模型拟合精度差，且多数方案需要修改原模型或依赖质量标注，落地门槛高。
### 方法关键点
1. 为黑盒外挂方案，无需改动原有模型结构，适配任意已有系统；
2. 无监督训练质量指数(QI)预测器，将可观测因素映射为QI，使同QI对应的误差服从近似高斯的条件分布，训练目标为分布匹配，无需质量标签；
3. 对每个QI单独拟合校准高斯误差模型，输出对应场景下的量化不确定性。
### 关键结果
在GPS误差预测、视觉姿态回归误差建模、世界模型预测误差三个任务中，相比全局单一高斯模型，condUQ大幅降低建模误差与实际误差分布的差异，学习到的QI与物理原理高度一致。
