---
title: 'The Paired Thermal Channel Is Two Orthogonal Axes: A Controlled Attribution
  Study of Calibration Cost and Detection Gain in Infrared Person Detection'
title_zh: 成对热通道正交双轴机制：红外行人检测校准与增益的受控归因研究
authors:
- Tian Zhang
- Yang Chen
- Bing Bai
- Weikai He
- Xiang Gao
- Zhirong Su
affiliations:
- School of Information Engineering, Shandong Management University
- School of Electrical and Electronic Engineering, Nanyang Technological University
arxiv_id: '2610.33118'
url: https://arxiv.org/abs/2610.33118
pdf_url: https://arxiv.org/pdf/2610.33118
published: '2026-10-23'
collected: '2026-11-01'
category: Other
direction: 红外行人检测·校准性能归因研究
tags:
- infrared-person-detection
- model-calibration
- evidential-deep-learning
- controlled-attribution
- performance-analysis
one_liner: 量化红外行人检测热通道双轴特性，明确校准成本与检测增益的影响因子
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有红外行人检测领域对热通道校准的信息增益、误差代价缺乏量化归因，二者的耦合作用机制尚未明确。
### 方法关键点
以温度证据学习(TEL)为测试床，设计五组受控对照实验，拆分配对对应关系、绝对校准尺度、空间结构三类核心变量，分别在校准误差、检测性能两个正交轴上开展归因分析，同时提出有限证据退化定理推导路由标量的闭式边界。
### 关键结果数字
- 真实校准ΔT比尺度匹配的灰度伪ΔT mAP高0.0221；
- 同时保留配对对应与校准尺度会使ECE从~0.05升至0.142，后校准仅能消除尺度带来的误差，配对带来的校准成本无法消除；
- 相位随机化破坏空间结构可在FLIR ADAS数据集上较真实ΔT再提0.0185 mAP。
