---
title: 'NaviCache: Test-Time Self-Calibration Caching for Video Generation'
title_zh: NaviCache：面向视频生成的测试时自校准缓存加速方法
authors:
- Zheqi Lv
- Zhibo Zhu
- Jinke Wang
- Qi Tian
- Shengyu Zhang
- Zhengyu Chen
- Chengxi Zang
- Zhou Zhao
- Fei Wu
affiliations:
- Zhejiang University
- Cornell University
- Tencent Hunyuan
- MeiTuan LongCat
arxiv_id: '2606.26795'
url: https://arxiv.org/abs/2606.26795
pdf_url: https://arxiv.org/pdf/2606.26795
published: '2026-06-25'
collected: '2026-06-27'
category: Other
direction: 扩散模型推理加速 · 测试时缓存
tags:
- Diffusion Model
- Video Generation
- Test-Time Acceleration
- Caching
- Inertial Navigation System
one_liner: 将视频扩散特征演化建模为惯性导航问题，提出即插即用的测试时自校准缓存实现误差有界推理加速
practical_value: '- 生成式推荐/广告的扩散类模型（如商品图、短视频生成）推理加速可借鉴：将迭代过程的特征演化建模为带动量的惯性系统，替代传统零阶近似缓存，降低观测噪声影响，在保证生成质量的前提下提升缓存命中率

  - 测试时自校准的无离线数据思路可迁移到电商动态生成场景：无需提前收集校准数据，避免用户/商品分布偏移导致的缓存失效，适配个性化、实时性要求高的生成任务

  - 双状态估计+不确定性感知的误差判定机制可复用：可用于LLM推理的KV cache有效性判断、推荐系统预计算缓存的动态淘汰，基于不确定性动态决定是否复用缓存，平衡延迟与效果'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**
视频扩散模型（VDM）迭代采样计算成本极高，严重制约实时部署。现有加速方案中，离线校准类依赖校准数据、耗时长、易受分布偏移影响；无离线校准类依赖瞬时零阶近似，易受观测噪声干扰，且忽略扩散轨迹的内在动量特性。

**方法关键点**
提出即插即用的测试时自校准缓存方法NaviCache，将扩散特征演化重构为惯性导航系统（INS）问题，通过建模输入输出变化的相对耦合，适配扩散过程的非平稳性与域间隙。核心采用双状态估计架构，自适应跟踪特征变化率及其潜在漂移，通过专属初始对齐阶段完成初始化；结合时间相关噪声调度与不确定性感知的测量更新机制，实现理论可证的误差有界计算跳过。

**关键结果**
在HunyuanVideo、Wan、Open-Sora三大视频扩散系列模型上验证，计算跳过的误差判断精度优于现有方法，综合性能表现优异。
