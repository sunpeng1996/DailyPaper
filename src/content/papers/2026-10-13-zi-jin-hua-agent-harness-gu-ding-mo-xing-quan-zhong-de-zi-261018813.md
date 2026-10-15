---
title: Self-Evolving Agent Harness
title_zh: 自进化Agent Harness：固定模型权重的自适应执行脚手架框架
authors:
- Chuyang Wei
- Haoxiang Guan
- Minghang Zhu
- Kexin Zhou
- Jiyan He
- Xiren Zhou
- Huanhuan Chen
- Yifei Shen
affiliations:
- Zhongguancun Academy
- Zhongguancun Institute of Artificial Intelligence
- University of Science and Technology of China
arxiv_id: '2610.18813'
url: https://arxiv.org/abs/2610.18813
pdf_url: https://arxiv.org/pdf/2610.18813
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: Agent 自进化框架与理论边界
tags:
- Self-Evolving Agent
- Harness Optimization
- Recursive Self-Improvement
- PAC Learning
- Agent Safety
one_liner: 提出固定模型下的Agent Harness自进化框架，给出分类体系、理论边界与系统设计规范
practical_value: '- 可复用Harness分层分类设计思路，将电商/推荐Agent的prompt、记忆、工作流、工具拆分为可迭代模块，无需修改模型权重即可快速迭代业务效果，降低适配成本

  - 验证Harness迭代效果可复用高概率准入规则：用独立新鲜验证集计算loss差，结合Hoeffding界控制过拟合风险，避免线上回归，适配电商大促等高稳定要求场景

  - 插件复用成本收益逻辑可直接迁移：首次生成工具的额外开销可在后续同类任务摊销，比如电商客服Agent生成常见咨询处理工具，5次任务即可节省11万+token、22.97s耗时

  - 落地自进化Agent可参考安全边界设计：将资金校验、紧急熔断等逻辑放在可编辑Harness之外，避免进化过程引发业务风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent迭代要么需要微调模型权重，成本高、可解释性差；要么零散优化prompt/工具，没有统一进化框架，无法保证迭代的泛化性与稳定性，也难以管控自进化带来的风险，亟需一套固定模型权重下的Harness自进化规范与理论支撑。

### 方法关键点
- 定义Harness为管控模型执行的软件与配置集合，包含执行控制、工具编排、上下文构建、内存管理等7大核心组件，自进化过程仅修改Harness，固定模型权重
- 分类梳理Harness可进化目标：分为解释层更新（指令、记忆、工作流）与执行层更新（工具代码、仓库逻辑、插件组合）两类
- 从进化优化与持续PAC学习角度推导理论边界：给出期望泛化界、历史回归预算约束下的保留界，以及基于独立新鲜验证集的高概率准入规则
- 明确自进化Agent安全设计原则：不可编辑评估函数、核心安全逻辑与可进化Harness解耦、持续验证应对分布漂移

### 关键结果数字
- 在SpreadsheetBench任务上，HarnessOpt+skill方案让GPT-5.4-nano准确率达77.58%，超过无Harness优化的GPT-5.5（76.20%），相比SkillOpt-Lite提升5.69~11.39个百分点
- 插件化自进化方案在多任务办公场景下，首次任务开销上升15.7%token、54.9%耗时，从第2个任务开始摊销成本，5个任务后累计节省110351token、22.97s耗时
- <40B参数量模型搭配EIP插件体系在LiveBrowseComp任务上得分51.39，超过同参数量最优基线48.7，性能逼近400B参数量模型水平

### 核心结论
固定模型权重的Harness自进化是比微调成本更低、可解释性更强、更易管控风险的Agent迭代路径，核心是做好进化目标分层、准入规则泛化性校验以及安全边界隔离。
