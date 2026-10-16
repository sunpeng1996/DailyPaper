---
title: Recursive Environment Scaling for General Long-Horizon Agents
title_zh: 面向通用长程Agent的递归环境缩放框架
authors:
- Lingxiao Jing
- Zhengbo Jiao
- Yichen Xiang
- Bofan Zhu
- Lingbei Meng
- Yan Ni
- Haorui Chen
- Ran Ran
- Zhirong Shen
- Yuheng Yang
affiliations:
- UESTC
- HKUST
- CUHK (SZ)
- THU
- NUS
arxiv_id: '2610.16397'
url: https://arxiv.org/abs/2610.16397
pdf_url: https://arxiv.org/pdf/2610.16397
published: '2026-10-11'
collected: '2026-10-16'
category: Agent
direction: 长程Agent 环境构建与训练优化
tags:
- Long-Horizon Agent
- Environment Scaling
- Agent Evaluation
- Supervised Fine-Tuning
- Task Difficulty
one_liner: 提出递归环境缩放RES框架，固定任务核心目标下可控提升Agent评测难度、优化SFT效果
practical_value: '- 训练电商客服、运营类长程Agent时，可复用RES思路：保留核心任务目标的前提下递归增加任务执行依赖复杂度，用更高难度轨迹做SFT，比原生轨迹最高提升14.61pp的任务成功率

  - 构建内部Agent评测基准时，可借鉴RES「proposer生成改造计划+执行校验+递归继承」流程，无需重新构造任务，仅改造现有基准就能得到更贴合真实复杂场景的评测集

  - 设计长程任务难度时，可参考RES的三类改造方向：调整信息获取路径、修改资源关联关系、增加执行前置依赖，可控提升难度而不改变核心考核目标'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前长程Agent的评测基准多为独立简单任务，难度调整容易改变核心考核目标，难以形成配对的评测/训练数据集；传统SFT使用原生任务轨迹训练，对长程复杂场景的泛化能力提升有限，亟需一种可控的环境缩放方法。
### 方法关键点
- 核心框架RES固定任务的核心目标、约束、完成条件，仅递归改造环境：proposer模块生成信息访问、资源关联、执行依赖三类改造计划
- 新增执行落地校验环节，验证候选环境是否保留原始任务有效性、改造点正常落地，失败则返回诊断信息引导修复
- 校验通过的环境作为父环境进入下一轮递归，改造点逐层继承累积，直到达到深度上限或难度阈值
### 关键实验
在3个主流Agent基准共294个任务上测试：6个主流大模型的任务成功率在RES缩放后平均下降57.14-77.14pp，其中DeepSeek-V4.1-Flash在Claw-Eval-Live上成功率从82.86%降至5.71%；用同等规模的RES轨迹做SFT，相比原生轨迹SFT在9组模型-基准对比中全部胜出，提升幅度7.00-14.61pp。
### 核心结论
在不改变任务核心目标的前提下，仅通过增加环境的执行依赖复杂度得到的训练轨迹，能显著提升长程Agent的泛化能力
