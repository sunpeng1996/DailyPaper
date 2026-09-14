---
title: 'PLC-DPO: Posterior Label Correction in Noisy and Ambiguous Preference Optimization'
title_zh: PLC-DPO：面向噪声模糊偏好优化的后验标签校正方法
authors:
- Boryeong Cho
- Sumyeong Ahn
- Se-Young Yun
affiliations:
- KAIST AI
- KENTECH
arxiv_id: '2608.30597'
url: https://arxiv.org/abs/2608.30597
pdf_url: https://arxiv.org/pdf/2608.30597
published: '2026-08-30'
collected: '2026-09-14'
category: Training
direction: 大语言模型对齐 · 鲁棒DPO优化
tags:
- DPO
- Preference Optimization
- Noisy Label
- Label Correction
- RLHF
one_liner: 无需额外监督，通过三态标签校正提升DPO在噪声偏好场景下的鲁棒性
practical_value: '- 做生成式推荐/Agent的LLM对齐时，若偏好标注存在噪声（如用户点击受位置bias、标注员分歧），可直接复用PLC-DPO的三态路由逻辑，无需额外过滤数据，既保留有效信号又避免错误梯度

  - 工程实现可复用EMA校准、stop-gradient路由、warm-up+置信度门控的训练trick，解决动态信号不稳定问题，不需要额外引入奖励模型，落地成本低

  - 电商推荐的pairwise排序场景（如A/B测试偏好对、点击序列正负样本对）存在大量模糊/反转样本，可将标签校正逻辑迁移到排序模型训练，替代样本过滤方案，提升排序鲁棒性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
DPO因无需训练独立奖励模型、实现简单可扩展，已成为LLM对齐的主流方案，但默认所有观测到的偏好对标签完全可靠，而真实场景中偏好数据普遍存在标注反转、标注员分歧、样本差异过小无明确方向等问题，会引入错误梯度导致对齐效果退化。现有鲁棒优化方案多为全局加噪或直接过滤可疑样本，既浪费有效信号，也未专门处理模糊无方向的样本。
### 方法关键点
- 为每个偏好对定义clean（原方向正确）、flip（原方向反转）、tie（无明确方向）三种隐状态，分别对应正向DPO、反向DPO、抑制方向梯度的tie正则三种损失
- 采用stop-gradient后的policy-reference margin作为路由证据，通过EMA在线校准margin的均值和方差，避免训练过程中信号尺度漂移
- 新增warm-up阶段（初期完全使用原生DPO训练）和路由置信度门控，仅当路由置信度达标时才引入校正损失，避免早期信号不可靠导致训练不稳定
- 最终损失为原生DPO和校正后损失的加权融合，无需额外监督信号或独立奖励模型
### 关键结果
跨57组数据集-模型-评测单元测试，PLC-DPO平均胜率达60.5%，较次优的rDPO高5个百分点；30%标签注入噪声场景下，胜率较基线高10个百分点以上；针对标注分歧的模糊tie样本，处理效果显著优于仅处理反转标签的方案。
### 核心结论
对于带噪声的pairwise偏好优化任务，主动校正标签方向和强度比单纯过滤可疑样本的信息利用率更高，鲁棒性更好
