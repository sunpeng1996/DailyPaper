---
title: 'VINCIE-NExT: Unlocking Video Editing from Images via In-Context Modeling'
title_zh: 《VINCIE-NExT：基于上下文建模实现图像到视频的编辑能力迁移》
authors:
- Leigang Qu
- Feng Cheng
- Ziyan Yang
- Bangbang Yang
- Zhaoyang Huang
- Wei Chow
- Yicong Li
- Wenjie Wang
- Tat-Seng Chua
- Yan Zeng
affiliations:
- National University of Singapore
- ByteDance Seed
- University of Science and Technology of China
arxiv_id: '2610.12104'
url: https://arxiv.org/abs/2610.12104
pdf_url: https://arxiv.org/pdf/2610.12104
published: '2026-10-08'
collected: '2026-10-10'
category: Multimodal
direction: 多模态视频编辑 · 跨域能力迁移
tags:
- In-Context Learning
- Video Editing
- Diffusion Model
- Cross-Domain Transfer
- Position Encoding
one_liner: 提出上下文建模框架VINCIE-NExT，迁移图像编辑能力到视频域，无需大规模配对视频编辑数据
practical_value: '- 可复用「成熟图像域能力迁移到视频域」的思路，解决电商商品短视频编辑标注数据不足的痛点，用已有的商品图编辑pair训练低成本视频编辑工具

  - 子任务链式拆分+测试阶段逐阶段扩散调优的范式，可迁移到AIGC推荐物料生成场景，无需重训即可通过增加计算量灵活提升生成质量

  - 跨上下文的共享空间坐标位置编码方法，可复用在多帧动态广告、商品展示视频生成场景，保障时序画面一致性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
视频编辑需标注的(source, instruction, edited)三元组成本极高、难以规模化生成，而图像编辑技术已成熟，拥有海量可用配对训练数据。
### 方法关键点
1. 拆解视频编辑为「视频→图像→图像→视频」可组合子任务链，将编辑意图路由到图像域，支持异构图像、视频语料在统一扩散目标下联合训练
2. 引入图像编辑pair作为上下文视觉演示，作为每帧输出的空间外观蓝图
3. 设计新型位置编码，在共享空间坐标系下关联图像演示与视频帧，实现外观变化在各帧的像素级一致传播
4. 编辑链推理策略支持测试阶段通过渐进式扩散阶段提升编辑质量，无需重训
### 关键结果
在OpenVE-Bench上实现全类别编辑任务SOTA性能，各消融实验验证所有组件有效性
