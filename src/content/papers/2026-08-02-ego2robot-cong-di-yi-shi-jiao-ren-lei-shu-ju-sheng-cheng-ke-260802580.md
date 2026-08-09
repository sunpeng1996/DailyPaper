---
title: 'Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data'
title_zh: Ego2Robot：从第一视角人类数据生成可扩展机器人训练数据
authors:
- Ye Wang
- Pei Lin
- Xiong-Hui Chen
- Haoqi Yuan
- Zhixuan Liang
- Yiyang Huang
- Anzhe Chen
- Zixing Lei
- Jie Zhang
- Tao Zhang
affiliations:
- AIM3 Lab, Renmin University of China
- Qwen Team, Alibaba Inc.
- ShanghaiTech University
- Beijing Institute for General Artificial Intelligence (BIGAI)
- Beijing University of Aeronautics and Astronautics
arxiv_id: '2608.02580'
url: https://arxiv.org/abs/2608.02580
pdf_url: https://arxiv.org/pdf/2608.02580
published: '2026-08-02'
collected: '2026-08-09'
category: Other
direction: 机器人数据合成 · VLA模型泛化优化
tags:
- Robot Data Synthesis
- Egocentric Video
- VLA Model
- Data Curation
- OOD Generalization
one_liner: 提出可扩展的第一视角人类操作视频转机器人数据管道，生成超大规模数据集提升VLA模型泛化性
practical_value: '- 跨域数据增强的三级质量管控流程可复用：生成式推荐做异构数据转训练样本时，可参考「语义对齐→内容生成→多级质量过滤」的管道，降低低质量生成样本对模型的干扰

  - 分布外泛化评估的维度拆解思路可借鉴：评估推荐模型跨场景/跨人群泛化性时，可将扰动拆解为内容外观、交互场景、模态形态、任务语义4个独立维度，精准定位模型短板

  - 低成本大规模预训练数据构造思路可迁移：业务侧标注数据稀缺时，可引入公开异构行为数据做语义对齐后生成预训练样本，降低数据采集成本同时提升小任务泛化性'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
机器人VLA（视觉-语言-动作）模型的泛化能力受限于真实机器人训练数据规模小、采集成本高，现有第一视角人类操作视频转机器人数据的方法仅能支撑小样本单任务训练，无法验证大规模预训练价值。

### 方法关键点
提出Ego2Robot可扩展转换管道，通过三步处理生成高质量机器人训练数据：1. 人类操作动作到不同形态机器人的动作重定向；2. 机械臂视角的视觉内容合成；3. 多级质量校验过滤低质量样本。管道同时支持标注数据集和野生视频输入，生成覆盖15种机器人形态的18561小时训练数据，是当前规模最大的ego-to-robot数据集。同时扩展RoboTwin2.0评估基准，从视觉外观、场景布局、实体形态、任务语义4个独立扰动维度评估分布外泛化能力。

### 关键结果
合成数据与真实机器人数据联合预训练，在多类扰动下的分布外泛化效果均有稳定提升，相关收益已在真实机器人部署中验证。
