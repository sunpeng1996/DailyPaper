---
title: 'MoI-Bench: A Benchmark for Image Generation and Editing on Mobile Devices'
title_zh: MoI-Bench：移动端图像生成与编辑基准测试集
authors:
- Kailai Feng
- Haoxiang Rao
- Yuxiang Wei
- Bo Chen
- Junsong Li
- Yang Pan
- Chengkun Cai
- Jagmohan Chauhan
affiliations:
- University College London
- Nanjing University
- The Hong Kong Polytechnic University
- East China Normal University
arxiv_id: '2610.37599'
url: https://arxiv.org/abs/2610.37599
pdf_url: https://arxiv.org/pdf/2610.37599
published: '2026-10-27'
collected: '2026-10-29'
category: Eval
direction: 端侧生成模型评估基准
tags:
- On-Device AI
- Benchmark
- Image Generation
- Image Editing
- Model Evaluation
one_liner: 提出面向移动端需求的图像生成编辑基准，含细粒度任务拆解与二维评估体系
practical_value: '- 端侧AIGC落地可复用Operation×Target细粒度任务拆解方法，针对电商海报修图、商品图生成等场景拆分操作与目标，精准定位模型能力缺口，避免笼统优化

  - 可借鉴质量-可部署性二维评估框架，替代单一得分排名，平衡端侧AIGC应用的效果与资源占用，适配移动端电商、广告类端侧生成需求

  - 实测结论可直接参考：当前端侧生成模型优先扩展任务覆盖度ROI高于继续压缩部署成本，重点补身份保留、文字渲染类能力短板，资源不足时可走端云协同路由'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有端侧图像生成编辑基准无法有效定位端侧与服务端模型的能力差，未结合移动端用户真实需求，模型优化指导颗粒度不足。

### 方法关键点
1. 构建MoI-Bench，基于移动端用户需求设计16种操作（移除、替换等）×8类视觉目标（人像、文字等）的正交轴，组合出64个子任务、1150个样本；
2. 配套MoI-Eval评估体系，覆盖指令遵循、视觉质量、细节保留3类任务专属准则，可聚合得到多维度能力画像；
3. 提出质量-可部署性二维能力图谱，替代传统单一得分排名，适配端侧落地需求。

### 关键结果
细粒度拆解可精准定位模型短板，例如文字替换优先级高于笼统的文字编辑优化；当前端侧模型已满足基础生成效率需求，优先扩展任务覆盖度的ROI高于进一步降低部署成本，身份保留、文字渲染是核心待补能力缺口。
