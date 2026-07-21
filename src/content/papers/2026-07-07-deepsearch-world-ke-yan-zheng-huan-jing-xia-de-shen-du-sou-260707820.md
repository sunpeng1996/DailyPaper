---
title: 'DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable
  Environment'
title_zh: DeepSearch-World：可验证环境下的深度搜索Agent自蒸馏框架
authors:
- Xinyu Geng
- Xuanhua He
- Sixiang Chen
- Yanjing Xiao
- Fan Zhang
- Shijue Huang
- Haitao Mi
- Zhenwen Liang
- Tianqing Fang
- Yi R. Fung
affiliations:
- HKUST
- Tencent
- HKUST(GZ)
arxiv_id: '2607.07820'
url: https://arxiv.org/abs/2607.07820
pdf_url: https://arxiv.org/pdf/2607.07820
published: '2026-07-07'
collected: '2026-07-21'
category: Agent
direction: 搜索Agent · 自进化训练
tags:
- Agent
- Self-Distillation
- Tool-Use
- Search Agent
- Self-Evolution
one_liner: 提出可验证离线搜索环境与自蒸馏框架，无需强模型蒸馏即可训练高性能开源搜索Agent
practical_value: '- 业务中搭建搜索/导购Agent时，可先基于垂直领域知识库（如电商商品库、服务规则库）构建可验证离线模拟环境，用自蒸馏迭代优化，无需依赖强Teacher生成的标注数据，大幅降低训练成本

  - 可复用轨迹转换trick：将带环境反馈、规划状态的高质量轨迹转换为标准ReAct格式训练数据，把规划、错误恢复、记忆跟踪能力注入普通ReAct Agent，无需修改推理阶段的工具调用逻辑，兼容性极强

  - 自进化训练工程可借鉴异步生成+双层过滤（先校验答案正确性，再过滤冗余轨迹）+多轮数据指数衰减采样的方案，既保证训练数据质量，又缓解灾难性遗忘，适合长周期Agent迭代

  - 电商复杂query搜索、多轮导购场景可借鉴其多跳QA构造思路，基于商品/服务实体的关联关系生成训练数据，覆盖更多用户长链路需求的推理路径'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有工具型Agent自进化方案存在三大核心痛点：基于SFT的方案依赖固定Teacher蒸馏的轨迹，性能易受基座能力、轨迹多样性限制；基于RL的方案奖励稀疏，无法定位工具调用、query改写、证据提取等环节的具体错误；现有自蒸馏方案缺乏稳定可验证的环境，中间步骤监督信号噪声大，难以落地到长horizon搜索场景。

### 方法关键点
- 构造DeepSearch-World可验证离线环境：基于Wikipedia实体关联生成420K多跳QA任务，配套确定性离线搜索、网页浏览工具，支持每一步工具调用的实体级进度校验，自动生成错误反思信号
- 设计脚手架Teacher生成高质量轨迹：分为规划、执行、结束三个阶段，显式记录子目标完成状态、待办列表、失败经验、已获取证据等结构化信息，产出带完整过程监督的轨迹
- 迭代自蒸馏训练流程：每轮用当前模型作为Teacher生成轨迹，先过答案正确性校验+轨迹质量过滤，再把脚手架轨迹的状态、环境反思转换成标准ReAct格式的<think>推理内容，用SFT更新学生模型，多轮迭代用指数衰减采样混合历史轮次数据缓解遗忘

### 关键结果
基于Qwen3.5-9B基座训练的DeepSearch-World-9B，对比基座性能全面提升：BrowseComp从7.4%升至31.2%，GAIA从23.9%升至61.5%，HotpotQA从45.3%升至93.4%，性能追平同量级开源SOTA搜索Agent。

**最值得记住的一句话**：可验证的过程级监督，比依赖强Teacher的轨迹标注、稀疏奖励的RL方案，更适合低成本迭代长horizon工具型Agent。
