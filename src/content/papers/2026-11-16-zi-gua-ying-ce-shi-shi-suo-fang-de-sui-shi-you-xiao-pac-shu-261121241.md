---
title: Anytime-Valid PAC-Bayes Certificates for Adaptive Test-Time Scaling
title_zh: 自适应测试时缩放的随时有效PAC-Bayes证书
authors:
- Xiaoyu Li
- Jiangxuan Long
affiliations:
- University of New South Wales
- The University of Hong Kong
arxiv_id: '2611.21241'
url: https://arxiv.org/abs/2611.21241
pdf_url: https://arxiv.org/pdf/2611.21241
published: '2026-11-16'
collected: '2026-11-17'
category: Eval
direction: 自适应推理 · 风险边界校准
tags:
- PAC-Bayes
- Test-Time Scaling
- Adaptive Inference
- Risk Calibration
- LLM Inference
one_liner: 提出适配自适应测试时缩放的随时有效PAC-Bayes证书，解决自适应选择后标准误差界失效问题
practical_value: '- 做LLM驱动的Agent推理、生成式推荐prompt选择/多步采样时，可复用该PAC-Bayes证书方法校准选择后的风险，避免自适应调优带来的验证乐观偏差

  - 多输出聚合（如召回结果重排投票、生成式推荐多候选选优）场景可复用文中的边际定律，判断算力投入的收益阈值，避免无效算力浪费

  - 自适应推理资源分配场景可直接复用文中的注水定律，做最优算力分配，平衡推理成本与效果'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
测试时缩放系统需自适应选择采样次数、prompt、验证器或聚合规则，反复查看校准集的行为会导致标准验证误差界失效，无法准确衡量部署后真实风险。
### 方法关键点
将测试时缩放流程建模为带随机成本的随机预测器，证明时间一致的PAC-Bayes证书，可同时覆盖所有校准时间、所有流程后验混合、所有数据依赖停止规则；有限搜索空间下惩罚项为log M/n，非均匀先验和局部后验混合可获得更紧边界；针对自洽性场景推导边际定律与最优算力分配的注水定律。
### 关键结果
GSM8K、MATH-500实验中，标称5%水平下传统最优选择误差界有22.5%的概率低于切分外真实风险，该证书从未失效；全GSM8K测试集上证书边界收紧至0.109（真实留出风险0.039）
