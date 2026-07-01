---
title: 'World Narrative Model for Highly Controllable Video Generation: A Paradigm
  Shift from Pixel Sampling to Physical World Orchestration'
title_zh: 面向高可控视频生成的世界叙事模型：从像素采样到物理世界编排的范式转变
authors:
- Ye Chen
- Xuanhong Chen
- Yupeng Zhu
- Liming Tan
- Zhewen Wan
- Yuxuan Xiong
- Tielong Wang
- Jinfan Liu
- Wuze Zhang
- Xiongzhen Zhang
affiliations:
- 上海交通大学
arxiv_id: '2606.31946'
url: https://arxiv.org/abs/2606.31946
pdf_url: https://arxiv.org/pdf/2606.31946
published: '2026-06-30'
collected: '2026-07-01'
category: MultiAgent
direction: 多Agent协作可控视频生成范式
tags:
- Controllable Video Generation
- Collaborative Agents
- 4D World Representation
- Modular Framework
- Multimodal Input
one_liner: 提出物理叙事与像素渲染解耦的WNM范式，大幅提升视频生成可控性与创作者意图匹配度
practical_value: '- 可复用「结构化参数蓝图+基础模型渲染」的解耦架构，迁移到电商商品短视频、信息流广告素材自动生成场景，大幅降低素材生成的试错成本

  - 多Agent协作将稀疏用户输入转换为可编辑定量参数的思路，可复用在广告创意生成pipeline，支持运营对素材元素、镜头、时长等属性的精细化调整

  - 模块化可插拔的组件设计思路，可迁移到生成式推荐系统中，实现用户意图理解、候选内容生成、渲染输出等模块的独立迭代与升级'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有工业级视频生成核心痛点是可控性不足：传统方案将视频视为像素分布采样问题，跳过显式实例级4D（3D+时间）物理世界建模，创作者无法定量指定几何、运动、相机、光照等参数，反复试错的「抽卡」模式导致专业内容生产成本极高。
### 方法关键点
提出World Narrative Model（WNM）范式，将待渲染的结构化物理叙事与像素生成过程完全解耦：用协作Agent将文本、参考视频、草图等稀疏多模态输入，转换为包含场景几何、物体布局、角色运动、相机轨迹、光照参数的可编辑4D世界表示作为确定性生成蓝图；驱动冻结或轻量适配的现有视频基模型作为神经渲染器输出最终视频，配套支持专业创作者微调的人机协作平台。
### 关键结果
大幅降低生成的概率性试错次数，输出视频的空间布局、角色运动、运镜效果与创作者意图匹配度显著提升；框架为开放模块化设计，世界表示、控制Agent、适配层等组件可独立迭代优化。
