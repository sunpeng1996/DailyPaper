---
title: 'VideoGen-Agent: Reinforcing Video Generation Agents'
title_zh: VideoGen-Agent：基于强化学习的视频生成智能体
authors:
- Binxu Li
- Haoyi Duan
- Yuhui Zhang
- Yaohui Zhang
- Zihao Lin
- Kaituo Feng
- Suozhi Huang
- Xiangyi Li
- Yu Li
- Chunyuan Li
affiliations:
- Princeton University
- Stanford University
- UC Davis
- MMLab, CUHK
- GWU
arxiv_id: '2609.24997'
url: https://arxiv.org/abs/2609.24997
pdf_url: https://arxiv.org/pdf/2609.24997
published: '2026-09-20'
collected: '2026-09-22'
category: Agent
direction: 生成式Agent · 工具调用强化学习优化
tags:
- Agent
- Reinforcement Learning
- Video Generation
- Tool Use
- Multimodal
one_liner: 通过多任务强化学习训练多模态Agent调度外部工具解决复杂视频生成的一致性、准确性问题
practical_value: '- 工具调用Agent的两阶段训练范式（SFT蒸馏教师轨迹+GRPO强化学习微调）可直接迁移到电商商品生成Agent、广告素材生成Agent开发，解决生成内容的事实性、一致性问题

  - 多任务混合奖励机制（格式校验+结果质量+工具使用合理性分权重加权）可复用在各类业务Agent的RL训练中，平衡工具调用正确性和最终业务效果

  - 通用工具接口设计思路值得借鉴：业务Agent训练完成后可直接升级下游工具（比如生成模型、检索库）无需重新训练Agent，大幅降低迭代成本

  - VABench的分能力维度评测思路可迁移到生成式推荐系统的效果评测，针对实体识别、物理合理性、时序逻辑等细分维度构建专项评测集'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视频生成模型依赖预训练内置知识，无法满足需要专业知识、特定实体身份保留、物理一致性、时序事件顺序的生成需求，难以落地到电商商品演示、广告素材、教育内容等业务场景。

### 方法关键点
- 设计三类统一接口工具集：增强工具（文本/图像检索、物理仿真）、生成工具（T2V/I2V/R2V/M2V多条件生成）、验证工具（目标检测、深度估计），支持不同生成任务需求
- 两阶段训练范式：第一阶段基于16K大模型蒸馏的工具调用轨迹做SFT初始化策略，第二阶段用GRPO做多任务强化学习微调；混合奖励由10%格式校验、50%VLM视频质量评分、40%工具使用合理性加权组成，加入任务级优势归一化平衡不同任务训练信号
- 多轮交互工作流：Agent根据prompt和中间工具返回结果自主决策，完成信息收集、生成、验证、迭代全流程，无需预设固定路径

### 关键实验
- 构建VABench评测集，含600条prompt覆盖程序知识、单/多实体身份保留、物理仿真、场景组合、多镜头时序6类任务
- 与10余款开源/闭源视频生成基线对比，使用Toolset1时比基础生成器Seedance 1.0提升19.1分（56.5→75.6），升级为Toolset2无需重新训练Agent，得分进一步提升到86.1，人类偏好超过最强基线的比例达84.3%

### 核心结论
工具增强Agent的能力上限不仅取决于Agent本身策略，还可通过升级下游工具无成本提升，两者发展互补而非替代
