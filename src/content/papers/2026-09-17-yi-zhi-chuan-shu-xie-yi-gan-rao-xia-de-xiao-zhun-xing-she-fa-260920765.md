---
title: Calibrated RF-Fingerprinting Under Interference With Heterogeneous Transmission
  Protocols
title_zh: 异质传输协议干扰下的校准型射频指纹识别方法
authors:
- Tariq Abdul-Quddoos
- Xiangfang Li
- Lijun Qian
affiliations:
- Prairie View A&M University, Texas A&M University System
arxiv_id: '2609.20765'
url: https://arxiv.org/abs/2609.20765
pdf_url: https://arxiv.org/pdf/2609.20765
published: '2026-09-17'
collected: '2026-09-21'
category: Other
direction: 射频指纹识别 · 多干扰场景校准
tags:
- RF-Fingerprinting
- 1D-CNN
- Model-Calibration
- Multi-label-Classification
- Spectrum-Monitoring
one_liner: 面向同信道多协议干扰场景，提出带假阴性上界保障的校准1D-CNN射频指纹识别方案
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有RF指纹识别研究仅适配单发射机场景，无法覆盖真实环境下同信道多信号时域、频域重叠的干扰场景，且缺乏识别结果可靠性保障。
### 方法关键点
1. 将多干扰下多发射机识别转化为多标签分类问题，采用1D-CNN作为基础识别模型；
2. 对模型输出概率做校准，推导标签概率置信阈值，给出平均假阴性数上界保证，避免漏判频谱违规行为。
### 关键结果
在POWDER 5G测试台真实数据（覆盖802.11a Wi-Fi、4G LTE、5G NR三类波形）上验证：校准后准确率随信道条件在73%~97%区间波动；校准后微召回率近似等于1减去校准假阴性上界，对分布外干扰鲁棒，适配高冲突真实无线环境。
