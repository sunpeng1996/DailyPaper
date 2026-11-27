---
title: 'TIDE-Flow: Fine-Grained Temporal Evidence and Structured Displacement Matching
  for Spike Optical Flow'
title_zh: TIDE-Flow：面向脉冲光流的细粒度时间证据与结构化位移匹配方法
authors:
- Hanwen Liang
- Wenxuan Liu
- Wenxin Huang
- Jingling Yuan
- Zhaofei Yu
- Xian Zhong
- Tiejun Huang
affiliations:
- Wuhan University of Technology
- Peking University
- Hubei University
arxiv_id: '2611.34854'
url: https://arxiv.org/abs/2611.34854
pdf_url: https://arxiv.org/pdf/2611.34854
published: '2026-11-25'
collected: '2026-11-27'
category: Other
direction: 脉冲相机高速场景光流估计
tags:
- Spike Camera
- Optical Flow
- Motion Estimation
- Temporal Modeling
- Feature Matching
one_liner: 提出融合时间积分证据与位移编码的脉冲光流框架，提升高速运动估计精度
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
脉冲相机通过积分触发机制捕获高速运动无曝光模糊，但二进制流编码累计光照而非瞬时强度，可靠运动估计难度大；现有方法的时间聚合操作会损失细粒度触发模式，基于相关性的估计器未显式表征候选位移的空间分布与歧义性。
### 方法关键点
1. 提出TIDE-Flow脉冲光流估计框架，融合时间积分证据(TIE)与位移证据编码(DEE)两个核心模块
2. TIE模块结合原始脉冲模式、多尺度触发统计、时间矩、边界感知间隔线索，在空间特征压缩前保留互补时序信息
3. DEE模块集成结构化候选网格特征与显式位移统计，表征匹配几何结构与竞争对应关系
4. 两个模块嵌入差分相关循环优化框架，实现时序运动建模与对应关系估计
### 关键结果
大量公开数据集实验验证框架有效性，控制变量消融实验证实两类证据建模模块的独立增益
