---
title: 'GraphVid: Interactive Graph-Controllable Video Generation'
title_zh: GraphVid：基于交互图的可交互可控视频生成方法
authors:
- Vedant Shah
- Onkar Susladkar
- Tushar Prakash
- Kiet Nguyen
- Tianjio Yu
- Adheesh Juvekar
- Muntasir Waheed
- Ismini Lourentzou
affiliations:
- University of Illinois Urbana-Champaign
- Sony Research India
arxiv_id: '2607.21580'
url: https://arxiv.org/abs/2607.21580
pdf_url: https://arxiv.org/pdf/2607.21580
published: '2026-07-22'
collected: '2026-07-24'
category: Multimodal
direction: 多模态可控视频生成 · 图条件驱动
tags:
- Controllable Video Generation
- Scene Graph
- Diffusion Model
- Multimodal Generation
- Dataset
one_liner: 推出交互图条件的图像转视频生成框架与标注数据集，实现多主体高精度可控视频生成
practical_value: '- 电商短视频生成场景可复用交互图条件逻辑：预定义商品、人物、场景的关系图谱，直接生成符合要求的带货短视频，无需复杂prompt调优

  - 多主体交互内容生成任务可借鉴结构化语义接口范式：替代纯文本prompt，解决多实体交互描述模糊、生成结果不符合预期的问题

  - 小样本可控生成场景可复用「冻结大模型+轻量条件控制模块」架构，显著降低训练成本与参数量需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有可控视频生成依赖文本prompt或轨迹输入，多主体交互描述模糊，轨迹标注成本随场景复杂度指数上升，遮挡重叠场景下歧义高。
### 方法关键点
1. GraphVid是图条件图像转视频生成框架：先从输入帧自动构建场景交互图，用户可编辑图中实体关系作为控制信号，转换为条件token引导冻结的视频扩散backbone生成结果
2. 配套发布GraphVid-Bench大规模交互中心视频数据集，包含结构化关系标注，可支撑同类交互感知视频生成模型训练
### 关键结果
训练数据量与参数量远低于现有运动控制方法的前提下，较Motion-I2V FID最高降低39.9%、FVD降低37.6%，PSNR从9.87提升至15.98，SSIM从0.38提升至0.61
