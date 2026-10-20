---
title: 'Agent World Model in the Wild: Computer-Use Agent Environment Synthesis'
title_zh: 面向通用计算机操作Agent的开源环境与任务合成管线WildAWM
authors:
- Zhaoyang Wang
- Qianhui Wu
- Haorui Wang
- Simon Yu
- Baolin Peng
- Canwen Xu
- Hao Cheng
- Wenlin Yao
- Boyi Liu
- Yite Wang
affiliations:
- UNC-Chapel Hill
- Microsoft Research
- Georgia Tech
- Northeastern University
- Independent Researcher
arxiv_id: '2610.26828'
url: https://arxiv.org/abs/2610.26828
pdf_url: https://arxiv.org/pdf/2610.26828
published: '2026-10-19'
collected: '2026-10-20'
category: Agent
direction: 计算机操作Agent · 合成训练环境构建
tags:
- Computer-Use Agent
- Environment Synthesis
- Reinforcement Learning
- Open Source
- Cross-interface Task
one_liner: 全开源管线生成跨GUI/MCP/CLI的计算机操作Agent训练环境任务，训练模型在8个OOD基准平均涨点超8分
practical_value: '- 任务合成质量门可直接复用：开发电商导购Agent、多工具调用运营Agent时，可照搬「异质Agent rollout+多Judge一致性校验+反事实探针」的校验逻辑，确保训练任务可解、难度适中、验证器可靠，避免无效训练

  - 跨模态联合训练范式可迁移：若业务Agent需同时操作后台CLI、商家GUI、内部工具API，可参考其多接口联合训练方案，相比单模态训练OOD泛化能力平均提升8-10个百分点

  - 长流程RL奖励设计可落地：电商大促自动化、商家批量操作等长horizon Agent训练，可采用「全任务成功满奖励+子任务检查点部分奖励+格式错误惩罚」的机制，有效解决信用分配问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前计算机操作Agent（CUA）训练依赖真实环境交互，存在安全风险高、状态难重置、成本昂贵的问题；人工构建的训练环境规模有限，现有合成方案多局限单一交互模态、依赖闭源前沿模型，无法支撑通用CUA的大规模强化学习训练。
### 方法关键点
- 全开源环境合成：基于生成的用户persona扩展多日活动轨迹，用开源编码Agent构建包含GUI网页、MCP服务、本地文件的完整PC环境，支持多接口联合交互
- 五级质量门控的跨接口任务生成：依次通过多样性筛选、初始状态不满足校验、异质Agent rollout验证可解性、无提示成功率控制难度、反事实探针校验验证器鲁棒性，确保任务质量
- 长horizon RL训练优化：采用「子任务检查点部分奖励+格式错误惩罚」的奖励机制，搭配动态rollout采样策略，解决长流程任务的信用分配问题
### 关键结果
- 合成341个长horizon跨接口任务，平均需要3.1次接口切换，前沿模型GPT-6-Astra通过率仅60%，难度足够支撑前沿模型训练
- 用合成数据训练的Qwen3.6-35B和Qwen3.5-4B模型，在8个分布外基准（覆盖网页/Claw/通用CUA）上平均分别涨点10.58、8.21，35B模型性能追平GLM-5.2，在部分基准上超过GPT-5.5
### 核心结论
仅用开源模型就能生成高质量的通用Agent训练环境与任务，训练出的模型泛化能力可逼近闭源前沿模型，大幅降低计算机操作Agent的研发门槛
