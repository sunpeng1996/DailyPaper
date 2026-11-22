---
title: In Situ Training of Optical Neural Networks by Coding Agents
title_zh: 基于编码Agent的光神经网络原位训练方法
authors:
- Ilker Oguz
- Colin Christian
- Christophe Moser
- Demetri Psaltis
- Gordon Wetzstein
affiliations:
- Stanford University
- Ecole polytechnique fédérale de Lausanne
arxiv_id: '2611.23875'
url: https://arxiv.org/abs/2611.23875
pdf_url: https://arxiv.org/pdf/2611.23875
published: '2026-11-17'
collected: '2026-11-22'
category: Agent
direction: Agent 硬件神经网络优化训练
tags:
- Coding Agent
- Optical Neural Network
- In Situ Training
- LLM for Science
- Hardware Optimization
one_liner: 提出optics as code方法，用编码Agent无需逐设备校准或硬件梯度即可高效训练光神经网络
practical_value: '- 可借鉴编码Agent自动调参的思路，替代无梯度搜索优化推荐系统超参数（如召回/排序阈值、特征权重），无需手动构建复杂校准模型

  - 可复用「Agent基于观测结果迭代假设、自动输出调整方案」的框架，用于推荐/广告线上A/B实验自动调优，降低人工介入成本

  - 端侧部署的推荐模型可参考该方法，在无法获取反向传播梯度的场景下实现高效小样本微调'
score: 4
source: huggingface-daily
depth: abstract
---

# 动机
光神经网络具备高速低功耗的计算优势，但实际硬件存在制造误差、器件失准等问题，现有原位训练方案要么需要逐设备手动构建校准数字模型，要么依赖低效的无梯度试错，落地成本高。
# 方法关键点
提出optics as code框架，调用可编写执行代码的Coding Agent，仅基于硬件返回的观测图像迭代调参，每次请求对应一个参数调整假设，无需硬件梯度或预校准模型；Agent可自主形成光学物理认知，用可解释的光学元件重参数化网络。
# 关键结果
分类、图像编码任务上性能优于所有无梯度方法，接近带校准模型的反向传播训练效果，成本仅为后者的极小部分，且性能随基础LLM能力提升同步优化，可支撑大规模光神经网络落地。
