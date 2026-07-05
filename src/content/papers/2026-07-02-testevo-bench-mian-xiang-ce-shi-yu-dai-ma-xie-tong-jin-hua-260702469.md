---
title: 'TestEvo-Bench: An Executable and Live Benchmark for Test and Code Co-Evolution'
title_zh: TestEvo-Bench：面向测试与代码协同进化的可执行动态基准
authors:
- Jiale Amber Wang
- Kaiyuan Wang
- Pengyu Nie
affiliations:
- University of Waterloo
- Google
arxiv_id: '2607.02469'
url: https://arxiv.org/abs/2607.02469
pdf_url: https://arxiv.org/pdf/2607.02469
published: '2026-07-02'
collected: '2026-07-05'
category: Agent
direction: Agent评测 · 软件自动化测试
tags:
- Agent Evaluation
- Test Generation
- Code Evolution
- Benchmark
- LLM Agent
one_liner: 推出覆盖测试生成/更新双赛道、支持可执行度量、防数据泄露的代码测试协同进化Agent评测基准
practical_value: '- 做Agent业务评测时可参考带时间戳的动态基准设计，仅使用模型训练截断后产生的任务做评估，从根源避免数据泄露导致的评测结果虚高

  - 评估Agent输出有效性时可替换静态匹配度量为可执行的真实结果度量，比如推荐/广告场景的真实点击转化率、代码场景的运行通过率，评估结果更贴合业务实际

  - 多场景Agent评测可参考分赛道任务设计，按任务类型/难度拆分评测集，更容易定位模型/Agent架构的短板，针对性迭代优化'
score: 4
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有测试生成/更新基准隔离测试与代码变更，依赖静态元数据，无法验证测试可执行性与语义关联性，也易存在训练数据泄露问题，难以准确评估测试自动化Agent能力。
**方法**：从开源仓库真实提交历史挖掘任务，分测试生成、测试更新双赛道，每个任务配套完整环境配置，支持通过率、覆盖率、变异分数等可执行度量；基准为动态设计，每个任务自带时间戳，通过自动化pipeline定期新增任务，评测时可筛选模型训练截止时间后发布的任务，大幅降低数据泄露风险。
**结果**：当前快照覆盖152个开源Java项目的746个测试生成、509个测试更新任务；SOTA Agent测试生成成功率最高达77.5%，测试更新最高达74.6%；在最新发布的任务、单任务资源受限场景下，成功率出现显著下跌。
