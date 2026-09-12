---
title: 'LangStreet: Persistent Language Fields for Anchor-Decoded Street Gaussians'
title_zh: LangStreet：锚点解码街道高斯场景的持久语言场构建方法
authors:
- Runyi Yang
- Deheng Zhang
- Xiaoye Wang
- Mengjiao Ma
- Lei Sun
- Kanzhi Wu
- Ajad Chhatkuli
- Luc Van Gool
- Danda Pani Paudel
affiliations:
- INSAIT, Sofia University “St. Kliment Ohridski”
- vivo Mobile Communication Co., Ltd.
arxiv_id: '2609.11616'
url: https://arxiv.org/abs/2609.11616
pdf_url: https://arxiv.org/pdf/2609.11616
published: '2026-09-10'
collected: '2026-09-12'
category: Other
direction: 3D高斯场景 · 语言语义场构建与压缩
tags:
- Gaussian Splatting
- Language Field
- 3D Scene Understanding
- Feature Compression
- Multimodal Retrieval
one_liner: 提出基于语义所有权的持久语言场，精度几乎无损下大幅压缩3D高斯场景语义存储开销
practical_value: '- 锚点主特征+低秩残差的分层存储思路，可迁移到大规模推荐系统的用户/物品语义特征存储场景，精度几乎无损前提下降低70%+存储开销

  - 弱支撑特征用锚点对齐证据补全的思路，可复用在推荐系统冷启动商品的语义特征补全任务中

  - 多视角观测语义聚合的所有权路由机制，可借鉴到多模态商品搜索的跨视角特征对齐链路'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有语言高斯场默认语义基元跨视角可识别，该假设在可扩展锚点解码表示中失效：持久锚点生成的视图相关子高斯的几何、外观随相机变化，无法绑定稳定语义。
### 方法关键点
1. 核心提出**语义所有权**机制：瞬态子高斯仅负责路由观测，持久解码器槽与父锚点持有语言场
2. 用alpha合成责任在槽位累积方向证据，统计量可精确边际化到锚点
3. 弱支撑槽位用锚点对齐证据补全，槽位细节用锚点相对语义坐标下的低秩残差表示，推出base（锚点+压缩残差）、light（仅锚点）、max（全维度槽特征）三个版本
### 关键结果
- KITTI-360数据集上，base版本2D mIoU达34.19，仅比max版本低0.01，有效特征存储仅2.72GiB，相比max的12.90GiB降低78.9%
- 三类版本在vKITTI2、Waymo数据集上均保持一致的精度-存储tradeoff趋势
