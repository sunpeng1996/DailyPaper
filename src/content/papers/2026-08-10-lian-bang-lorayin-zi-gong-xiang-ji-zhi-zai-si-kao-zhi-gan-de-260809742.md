---
title: 'Rethinking Factor Sharing in Federated LoRA: A Rank-Aware Adaptive Approach'
title_zh: 联邦LoRA因子共享机制再思考：秩感知的自适应方法
authors:
- Xinyi Xu
- Bingnan Xiao
- Shuang Qin
- Gang Feng
- Tony Q. S. Quek
affiliations:
- University of Electronic Science and Technology of China
- Fudan University
- Singapore University of Technology and Design
arxiv_id: '2608.09742'
url: https://arxiv.org/abs/2608.09742
pdf_url: https://arxiv.org/pdf/2608.09742
published: '2026-08-10'
collected: '2026-08-11'
category: Training
direction: 联邦学习 · LoRA自适应因子共享
tags:
- LoRA
- Federated Learning
- Parameter-Efficient Fine-Tuning
- Adaptive Factor Sharing
- Rank-Aware
one_liner: 提出秩感知的RSS指标训练前自适应选择LoRA共享因子，构建FedAS-LoRA提升联邦微调效果
practical_value: '- 端侧个性化LLM微调（如电商端侧导购Agent、用户端个性化推荐大模型）场景下，无需硬编码固定共享A或B，可根据客户端数据分布自适应选择策略，同时降低通信成本、提升个性化效果

  - RSS指标设计思路可复用：多租户/多场景LLM微调时，用冻结backbone提取的表征计算全局与本地子空间能量差，快速判断共享输入侧还是输出侧参数，无需大量消融实验即可确定最优策略，节省试错成本

  - 联邦场景推荐大模型微调可直接复用FedAS-LoRA训练流程，仅上传选中的共享因子，通信量与固定共享策略持平，准确率平均提升近1个百分点'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有联邦LoRA方法均硬编码固定共享A或B因子，未考虑两类因子的结构不对称性，固定策略在不同数据分布、LoRA秩、客户端参与模式下易出现次优效果；同时联邦场景数据分散、隐私要求高，无法集中调参选择最优共享策略，亟需训练前即可自动确定共享方案的高效方法。

### 方法关键点
- 基于最小二乘代理分析发现：Share-A/Local-B要求所有客户端共享输入侧秩r子空间，Share-B/Local-A要求共享输出侧秩r子空间，两类策略的投影残差不同，应选择聚合残差更小的策略
- 设计训练免费的秩感知共享子空间充足性（RSS）指标：用冻结LLM backbone提取的序列表征，计算全局秩r子空间与本地客户端秩r子空间保留的表征能量比值，结合随机拆分校准、bootstrap校准得到阈值，判断全局输入子空间是否充足，决定共享A还是B
- 提出FedAS-LoRA框架，训练前用RSS确定共享策略，训练时仅上传选中的共享因子，另一因子保留在客户端，已证明在任意客户端参与模式下都可收敛到平稳邻域

### 关键结果
在GLUE基准（MNLI、SST-2等5个理解任务）和GSM8K生成任务上测试，对比LoRA、FFA-LoRA、FedSA-LoRA等基线：GLUE平均准确率达90.77%，较FedSA-LoRA高0.93个百分点；GSM8K上准确率达56.28%，较标准联邦LoRA高1.14个百分点；在不同客户端采样模式、数据异质性、LoRA秩下均稳定优于基线。

**最值得记住的一句话**：LoRA的A和B因子存在结构不对称性，联邦场景下没有普适的固定共享策略，根据数据分布和秩自适应选择才是最优解
