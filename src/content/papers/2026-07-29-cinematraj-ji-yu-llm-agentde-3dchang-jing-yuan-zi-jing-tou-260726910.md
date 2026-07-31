---
title: 'CinemaTraj: Composing Atomic Camera Trajectories for 3D Scenes with LLM Agents'
title_zh: CinemaTraj：基于LLM Agent的3D场景原子镜头轨迹组合生成
authors:
- Qianru Li
- Xuyang Chen
- Erkin Türköz
- Lu Liu
- Xuqin Wang
- Liqiu Meng
- Tao Wu
- Yanfeng Zhang
affiliations:
- Technical University of Munich
- Huawei Dresden Research Center
arxiv_id: '2607.26910'
url: https://arxiv.org/abs/2607.26910
pdf_url: https://arxiv.org/pdf/2607.26910
published: '2026-07-29'
collected: '2026-07-31'
category: Agent
direction: LLM Agent · 3D空间语义推理
tags:
- LLM Agent
- 3D Scene Graph
- Spatial Reasoning
- Trajectory Generation
- Parametric Representation
one_liner: 基于LLM Agent结合3D场景图实现自然语言驱动的3D场景镜头轨迹自动生成
practical_value: '- 可借鉴「复杂任务拆分为原子动作序列」的思路，将用户复杂导购/搜索需求拆解为标准业务原子动作，降低Agent执行出错率

  - 3D场景图作为结构化先验注入LLM Agent的思路可复用，如电商3D商品展示场景中，构建商品语义+几何的结构化知识底座，支撑智能导览Agent路径规划

  - 「语言指令→参数化执行模板」的映射方法可迁移到电商虚拟导购、3D家装/房产广告自动生成等场景，提升生成内容语义符合度'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有3D场景镜头轨迹生成方法要么依赖2D图像先验缺乏3D空间感知，要么仅做几何路径规划脱离电影语义，无法满足自然语言驱动的3D导览、广告制作等场景需求。
### 方法关键点
1. 将轨迹规划重构为语言对齐的空间推理任务，LLM Agent输入为用户prompt与结构化3D场景图
2. Agent将自然语言指令拆解为推镜头、环绕、升降等7类原子镜头动作，通过自研参数化轨迹表示实例化每类动作，同步支持避障优化
3. 额外生成与镜头运动对齐的语音旁白、字幕，直接输出带解说的成片
### 关键结果
在ScanNet++真实场景数据集上测试，相比现有方案，prompt对齐度、轨迹质量、安全性三类指标均实现领先，生成轨迹无碰撞、符合电影级质感
