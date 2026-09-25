---
title: 'WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation'
title_zh: WanPE：面向现代文本转视频生成的电影级提示增强方法
authors:
- Yubo Zhu
- Yawen Shao
- Ziyun Dai
- Zixun Fang
- Kai Zhu
- Siyang Sun
- Haolan Xue
- Chuxin Wang
- Tingyu Weng
- Jingming Luo
affiliations:
- Nanjing University
- Wan Team, Alibaba Group
- University of Science and Technology of China
- Fudan University
- Tsinghua University
arxiv_id: '2609.30221'
url: https://arxiv.org/abs/2609.30221
pdf_url: https://arxiv.org/pdf/2609.30221
published: '2026-09-23'
collected: '2026-09-25'
category: LLM
direction: 大模型提示增强 · 文本转视频生成
tags:
- Prompt Enhancement
- Text-to-Video
- GRPO
- Semantic Consistency
- LLM
one_liner: 397B参数电影级文本转视频提示增强模型，基于105万真实视频训练，大幅提升长视频生成用户偏好
practical_value: '- 可复用SC-GRPO的语义一致性对齐思路，优化电商商品短视频生成的提示增强模块，避免生成内容偏离商品核心卖点与用户原始需求

  - 视频驱动的反向构建提示优化方法可迁移到种草短视频prompt自动生成场景，基于爆款视频反向沉淀标准化镜头脚本模板，降本提效

  - 多镜头长序列语义保真方案可借鉴到AI导购Agent的多轮内容生成场景，保障多轮交互下用户需求不发生漂移'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前主流文本转视频（T2V）系统已支持生成30秒高质量内容，但用户输入的原始prompt普遍缺乏镜头规划、运镜、灯光等电影级要素，长视频生成的连贯性、需求符合度差，且缺少标准化的提示增强效果评估基准。
### 方法关键点
1. 训练397B参数的WanPE提示增强模型，基于1.05M真实视频数据学习导演级电影规划能力，通过视频grounded反向构造方式生成镜头级制作方案
2. 提出Semantic-Consistency GRPO（SC-GRPO）对齐算法，保障多镜头跨时间维度下用户原始需求的语义一致性
3. 构建人工标注测试集WanPEval，覆盖5-30秒不同意图粒度，包含约1.1万次盲测成对评估
### 关键结果
对接Wan3.0视频生成器时，WanPE-397B较原始prompt在5-15秒场景提升用户偏好10.66~18.84分，30秒场景大幅提升50.86分；反向构造效果显著优于正向改写，SC-GRPO在不同模型规模下均能稳定保障语义保真度，5-15秒场景效果超过所有参评商业方案，30秒场景与Seedance 2.5表现相当
