---
title: 'Plan4D: Generative Plannable 4D Worlds'
title_zh: Plan4D：可规划的生成式4D世界模型
authors:
- Hangwei Zhang
- Rujing Dang
- Ruimin Lin
- Jiahong Wu
- Xiangxiang Chu
- Chuanxia Zheng
affiliations:
- Nanyang Technological University
- Alibaba Group
arxiv_id: '2611.26516'
url: https://arxiv.org/abs/2611.26516
pdf_url: https://arxiv.org/pdf/2611.26516
published: '2026-11-19'
collected: '2026-11-21'
category: Multimodal
direction: 多模态生成 · 4D世界建模
tags:
- World Model
- 4D Generation
- Video Generation
- 3D Reconstruction
- Model Stitching
one_liner: 通过拼接视频生成与3D重建基础模型，实现带稠密4D几何信息的文本可控可规划世界生成
practical_value: '- 电商3D商品展示/虚拟试穿业务可复用模型拼接架构，耦合现有视频生成、3D重建预训练模型，低成本生成带几何信息的动态商品内容，无需全量重训

  - 具身Agent虚拟导购、3D直播场景可借鉴4D生成思路，实现文本可控的长时序虚拟人-商品交互场景生成，提升交互真实感

  - 内容平台商家工具侧可基于该方案搭建动态3D商品内容生成工具，降低商家制作商品展示视频、3D种草内容的成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有面向未来预测的世界模型普遍侧重生成视频的美学质量，缺乏显式4D建模，存在物理 grounding 弱、时序几何一致性差的问题，且带动作配对和稠密4D标注的训练数据天然稀缺。
### 方法关键点
1. 采用模型拼接架构，融合视频生成基础模型LongCat-Video与3D重建模型Depth Anything 3的互补先验，大幅降低对标注训练数据的依赖
2. 新增辅助DPT头实现场景流预测，可同步输出未来RGB视频、深度、相机参数、点云、场景流等稠密4D几何信息
3. 支持输入观测场景上下文+文本指定动作，生成可控的长时序、细粒度动态3D场景
### 关键结果
在合成和真实数据集上均取得生成式4D环境反应建模的SOTA性能，生成未来视频的视觉保真度和几何精度均实现大幅提升。
