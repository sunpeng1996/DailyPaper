---
title: 'StepBench: Diagnosing Real-World Procedural Understanding in AI Agents'
title_zh: StepBench：面向AI Agent的真实场景流程理解诊断基准
authors:
- Hossein A. Rahmani
- Bin Wu
- Chaeeun Lee
- Fanghua Ye
- Sahan Bulathwela
- Sujay Kumar Jauhar
- Marzieh Fadaee
- Nick Craswell
- Emine Yilmaz
affiliations:
- University College London
- University of Edinburgh
- Microsoft
- Cohere Labs
arxiv_id: '2610.26679'
url: https://arxiv.org/abs/2610.26679
pdf_url: https://arxiv.org/pdf/2610.26679
published: '2026-10-19'
collected: '2026-10-21'
category: Eval
direction: Agent 流程规划能力诊断基准
tags:
- Agent
- Benchmark
- Procedural Planning
- LLM Judge
- Evaluation
one_liner: 推出含6885个真实开放域流程的多任务基准，细粒度诊断AI Agent流程规划能力
practical_value: '- 做电商导购、售后、商家运营等场景的Agent任务规划时，可复用StepBench的5项诊断任务设计，先测缺步补全、错误检测、步骤排序能力，无需全流程上线即可预判规划效果，降低试错成本

  - 流程生成评估可复用STEPEVAL的Critical Failure判据，无需严格匹配参考流程，仅判断是否存在阻碍目标完成的致命错误，适配电商场景多合法流程的情况，还可蒸馏8B小模型做评估，成本大幅低于调用大模型

  - 做复杂长流程规划（如大促活动搭建、多步骤用户运营路径规划）时，需重点优化步骤排序能力：实测当前最强模型9步以上流程排序准确率仅33.1%，可将排序能力单独拆分构造微调数据，提升长流程规划可靠性

  - 可复用该论文的负例构造方法：生成同类别语义相似但不属于当前流程的干扰样本，用于优化推荐、搜索模型的细粒度差异识别能力'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent规划评测要么仅关注最终结果，无法区分缺步骤、错误步骤、顺序错误等不同失效模式；要么需要在仿真/形式化环境执行，开放域场景下无法规模化落地，亟需免执行、细粒度的规划能力诊断基准。
### 方法关键点
- 从wikiHow爬取1w+候选流程，经GPT-4.1过滤+人工校验，得到81个领域共6885条专家验证的标准流程，额外构造2026年新发布的214条流程作为防训练数据泄露的验证集
- 基于同一份流程衍生5项诊断任务：最后一步选择、缺步补全、错误步骤检测、步骤重排、下一步生成，覆盖规划全链路能力；新增全流程生成任务，关联诊断能力与端到端效果
- 推出STEPEVAL评估方案：定义阻碍目标完成的Critical Failure为判定标准，蒸馏得到8B参数的评估小模型，与人类标注吻合度达82.5%，评估成本远低于GPT-5
### 关键结果
- 评测12个模型14种配置，步骤重排是最难任务：最强模型GPT-5.6-sol整体排序准确率仅63.0%，9步以上长流程准确率跌至33.1%
- 诊断任务得分与全流程生成有效率强相关：步骤重排准确率和全流程有效率的斯皮尔曼相关系数达0.96，仅用低成本诊断任务即可预估模型端到端规划效果，无需全量生成+评估
- 2026年新流程验证集上，诊断任务得分平均下降不足1.5分，模型排序基本不变，证明基准不受训练数据泄露影响，结果可靠

**最值得记住的一句话**：Agent规划能力不能只看端到端效果，步骤排序、错误检测等细分能力的差异，才是决定复杂场景下规划可靠性的核心
