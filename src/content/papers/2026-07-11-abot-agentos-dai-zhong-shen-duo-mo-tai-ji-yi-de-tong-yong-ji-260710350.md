---
title: 'ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory'
title_zh: ABot-AgentOS：带终身多模态记忆的通用机器人Agent操作系统
authors:
- Jiayi Tian
- Shiao Liu
- Yuting Xu
- Jia Lu
- Zihao Guan
- Honglin Han
- Di Yang
- Minqi Gu
- Yifei Qian
- Tianlin Zhang
affiliations:
- Alibaba Group AMAP CV Lab
arxiv_id: '2607.10350'
url: https://arxiv.org/abs/2607.10350
pdf_url: https://arxiv.org/pdf/2607.10350
published: '2026-07-11'
collected: '2026-07-14'
category: Agent
direction: 具身Agent · 多模态终身记忆
tags:
- EmbodiedAgent
- Multi-modalMemory
- LifelongLearning
- Edge-CloudCollaboration
- AgentBenchmark
one_liner: 提出通用机器人Agent操作系统，配套终身多模态图记忆与具身评测基准，提升长时具身任务性能
practical_value: '- 多模态图记忆设计可迁移到用户行为建模：将用户浏览、点击、咨询、实拍等多模态行为转换为带类型、可溯源的结构化记忆图，检索时先匹配种子节点再扩展关联子图，比纯文本RAG召回更精准，适配个性化推荐、用户画像建模等场景。

  - 失败驱动的自进化机制可复用：将推荐/广告/Agent服务的bad case归因后生成受限格式的演进资产，严格按时间分桶校验，资产仅应用于后续分桶避免数据泄露，同时设置回归校验门槛，避免优化新问题时破坏已有正常逻辑。

  - 边云协同路由可落地到端侧智能业务：常规请求（如端侧个性化推荐、简单咨询）由端侧小模型处理，复杂任务（如跨session偏好召回、多步导购规划）按需调用云端大模型，兼顾低延迟与推理能力，降低服务成本。

  - 分阶段校验的执行框架可优化Agent任务成功率：将复杂任务拆分为主LLM规划、子Agent隔离执行、运行中/子任务/结束前三级校验的闭环，减少长时任务的停滞、提前终止、结果幻觉等问题。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前VLM/VLA已显著提升机器人的感知与动作预测能力，但长时具身Agent仍存在三大核心缺口：推理执行层面缺乏中间层承接任务拆解、容错、校验逻辑，常直接把模型输出映射到动作，稳定性差；跨形态适配层面系统与硬件强绑定，迁移成本极高；具身记忆层面现有文本缓存、短期缓冲区无法长期存储带时空关系、源溯源的多模态交互经验，同时缺乏标准化的长时具身任务评测基准。
### 方法关键点
- 架构采用边云协同分层设计：端侧Tiny LLM处理常规请求，复杂任务按需路由到云端大模型；Agent Harness拆分为主LLM场景化规划、Skill Runner隔离执行子任务、多阶段校验器（运行中/子任务/结束前三级校验）的闭环，解耦高层推理与底层硬件控制，适配人形机器人、四足机器人等多形态硬件。
- 记忆系统设计通用多模态图记忆：将对话、视觉观测、空间上下文、时序关系、任务轨迹转换为带源溯源的类型化节点与边；配套失败驱动的终身自进化机制，每个时间分桶的失败案例归因后生成演进资产，通过目标提升、回归校验双门槛后仅应用于后续分桶，避免数据泄露；采用边云分离的记忆管理，私有数据留驻端侧，公共知识同步云端，隐私分类准确率超99%。
- 推出EmbodiedWorldBench具身评测基准：覆盖16个室内/室外/混合场景、4个难度等级、200+长时具身任务，采用轨迹溯源的客观评分，避免人工打分偏差。
### 关键实验结果
记忆评测维度，静态版ABot-AgentOS在LoCoMo得87.5、OpenEQA EM-EQA得59.9、Mem-Gallery得88.6、NExT-QA Acc@All得76.5；自进化后LoCoMo提升至88.7、OpenEQA至60.4、Mem-Gallery至89.0，全面优于单控制器基线。
### 核心洞察
Agent系统的记忆不仅要存储内容，更要通过可审计的失败归因迭代记忆处理流水线，才能实现真正的终身学习。
