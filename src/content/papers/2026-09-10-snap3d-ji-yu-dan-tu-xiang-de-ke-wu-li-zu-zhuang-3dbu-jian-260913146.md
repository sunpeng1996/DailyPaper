---
title: 'SNAP3D: Physically Grounded 3D Parts for Assembly from a Single Image'
title_zh: SNAP3D：基于单图像的可物理组装3D部件生成框架
authors:
- Yu-Rou Tuan
- Hao-Tang Tsui
- Nicolas Ugrinovic
- Kris Kitani
- Xiaoxuan Ma
affiliations:
- Carnegie Mellon University
arxiv_id: '2609.13146'
url: https://arxiv.org/abs/2609.13146
pdf_url: https://arxiv.org/pdf/2609.13146
published: '2026-09-10'
collected: '2026-09-14'
category: Other
direction: 单图像3D生成 · 物理约束优化
tags:
- 3D Generation
- Physics Constraint
- Assembly Generation
- Single Image Reconstruction
- Physical Simulation
one_liner: 提出物理引导的单图像3D部件生成框架，解决部件穿插、连接无效、重力下坍塌问题
practical_value: '- 3D电商商品建模、AR试穿/试用场景可复用物理约束校验逻辑，避免生成的3D商品模型存在部件穿插、结构不合理等问题

  - 虚拟商品DIY定制、组装类互动推荐场景可引入物理仿真反馈机制，优化生成的可组装部件参数，提升用户互动真实感

  - 生成式内容评估可参考其思路，在传统几何/视觉指标之外，补充真实场景可用性、物理有效性维度的校验规则'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有部件感知3D生成方法仅保证视觉层面的部件完整，未校验物理组装有效性，易出现部件穿插、连接无效、重力下坍塌等问题，无法支撑编辑、仿真、实体制造等下游场景。
### 方法关键点
1. 构建物理引导的单图像3D部件生成优化框架，先消除部件穿插问题，重建邻接部件接触图，在接触面引入参数化连接件
2. 引入物理仿真反馈，迭代优化连接件的位置、朝向、尺寸，在保留生成几何质量的前提下提升组装稳定性
3. 提出基于物理的评估协议，在传统几何指标之外直接校验重力下的组装有效性与稳定性
### 关键结果数字
对比多款主流部件感知3D生成器，物理可实现性与稳定性大幅提升，几何质量无明显下降，生成结果可直接3D打印并完成真实世界组装。
