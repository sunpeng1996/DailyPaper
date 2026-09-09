---
title: 'Task-Blind No MORE: Multi-Task Information Flow in Unified Ranking Backbones'
title_zh: MORE：解决统一排序backbone任务盲问题的多任务信息流方案
authors:
- Yuchen Wang
- Feng Niu
- Qing Tan
- Junting Lu
- Baoxin Wu
- Jun Gao
affiliations:
- Hello Group
- University of Science and Technology of China
- Institute of Software, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Beijing Information Science and Technology University
arxiv_id: '2609.07273'
url: https://arxiv.org/abs/2609.07273
pdf_url: https://arxiv.org/pdf/2609.07273
published: '2026-09-07'
collected: '2026-09-09'
category: RecSys
direction: 多任务排序 · 统一排序backbone优化
tags:
- Multi-Task Learning
- Ranking Model
- Unified Backbone
- Industrial Recommendation
- CTR Prediction
one_liner: 将多任务信息流嵌入统一排序backbone各层，实现任务信号与特征序列表示协同演化
practical_value: '- 多任务建模可复用Shared/Private Anchor Token设计，将任务信号下沉到backbone每层，替代传统仅塔层做任务分化的方案，解决任务盲结构性瓶颈

  - 特征交互阶段引入Task-Boundary Mask，隔离不同Private Anchor的信息交互，避免高频任务梯度污染低频任务表示，可直接适配电商点击/加购/转化等多任务场景的负迁移问题

  - 线上部署可直接复用请求级共享计算策略，同请求下用户侧序列计算跨候选批量复用，实测P99 latency降30%，适配高并发推荐/广告排序场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有统一排序backbone（如HyFormer、MixFormer）仅将多任务建模放在backbone后的预测塔层，backbone本身是任务盲的，存在三大核心问题：序列读取与特征交互无法适配不同任务的偏好差异；任务分化前存在共享表示的结构性瓶颈，塔层的专家/门控机制无法重构未被backbone编码的任务感知特征；单纯扩容模型规模时多任务收益边际衰减明显，参数利用率低。

### 方法关键点
- 引入Anchor Token作为跨层任务信息载体：Shared Anchors编码跨任务共性，Private Anchors每个任务对应1个，初始化时拼接行为序列池化结果与非序列特征，叠加任务先验嵌入增强区分度
- 每个MORE Block包含三个模块：任务感知序列读取（Anchor作为Query做交叉注意力读取行为序列，独立门控筛选适配任务的序列信号）；选择性语义混合（Anchor与非序列特征混合时叠加Task-Boundary Mask，仅允许Private Anchor与自身、Shared Anchor、非序列特征交互，避免跨任务语义污染）；任务增强（每个Private Anchor通过独立FiLM分支，用非序列特征做仿射变换增强任务特异性）
- 训练推理采用请求级共享计算：同请求下用户侧序列计算仅执行1次，跨候选批量复用，无需修改模型结构

### 关键实验
离线用陌陌附近Feed 90天工业数据，对比Transformer+RankMixer、STCA、MixFormer、HyFormer、OneTrans等SOTA基线，7个任务GAUC均最优，对比OneTrans FLOPs仅增0.12G，平均GAUC多提升0.18%；线上A/B测试实现用户使用时长+3%、评论率+3.6%、深聊率+2%，P99推理 latency降低30%，已全量部署到生产环境。

最值得记住的一句话：统一排序backbone的多任务优化，仅靠塔层的专家/门控机制存在结构性瓶颈，将任务信号下沉到backbone每层的收益远高于单纯扩容模型规模。
