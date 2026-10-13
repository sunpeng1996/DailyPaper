---
title: 'MotionCoach: Constructing Multimodal Guidance for Video Professional Motion
  Editing'
title_zh: MotionCoach：面向专业视频动作编辑的多模态引导构建
authors:
- Siyi Qian
- Hanqing Yang
- Weihuang Lin
- Zihao Yang
- Yichen Lu
- Yuanhong Zheng
- Sheng Li
affiliations:
- Peking University
- Alibaba Token Hub, Alibaba Group
- University of Science and Technology of China
- Zhejiang University
arxiv_id: '2610.12963'
url: https://arxiv.org/abs/2610.12963
pdf_url: https://arxiv.org/pdf/2610.12963
published: '2026-10-09'
collected: '2026-10-13'
category: Agent
direction: 多模态Agent · 专业视频动作编辑
tags:
- Multimodal Agent
- Video Editing
- GRPO
- SFT
- Self-Verification
- Reinforcement Learning
one_liner: 提出多模态Agent MotionCoach，无需重训视频编辑模型即可提升专业动作编辑精度
practical_value: '- 专业领域内容生成场景可复用「多轮工具调用+自校验」的Agent架构，无需重训下游基础模型即可注入垂直领域知识，适配电商专业商品展示视频制作、广告创意生成等需求

  - 小样本Agent训练可参考「10k量级SFT冷启动 + 2k量级GRPO强化学习微调」的范式，搭配覆盖内容质量、最终效果、输出格式的多维度奖励函数，大幅提升输出稳定性

  - 垂直场景效果评估可参考VPMEBench的构建思路，收集带细粒度标注的领域专属任务集，解决通用评估基准无法衡量垂直场景专业效果的问题'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视频编辑模型仅接收专业动作名称指令时，无法生成符合细粒度技术规范的体育、表演、武术等专业动作，重训基础模型成本高、泛化性差。

### 方法关键点
1. 设计多模态Agent MotionCoach，通过多轮工具调用+自校验生成事实准确的引导prompt与参考视频片段，直接注入下游视频编辑模型，无需重训基础模型。
2. 构建训练轨迹流水线，先基于10k条SFT数据冷启动，再基于2k条RL数据采用GRPO强化学习优化，奖励覆盖引导prompt质量、输出视频动作效果、输出格式三个维度。
3. 开源VPMEBench评估基准，包含314个带细粒度标注的专业动作编辑任务。

### 关键结果
在Seedance 2.0上整体编辑得分从55.1提升至65.6，在MiniMax-H3上从51.2提升至64.5
