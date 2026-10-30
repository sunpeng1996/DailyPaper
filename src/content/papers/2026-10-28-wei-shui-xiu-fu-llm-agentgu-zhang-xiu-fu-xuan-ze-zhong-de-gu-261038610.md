---
title: Repairs for Whom? Evaluator-Executor Mismatch in Selecting Repairs for Failed
  LLM Agents
title_zh: 为谁修复？LLM Agent故障修复选择中的评估者-执行者错配问题
authors:
- Yijun Liao
- Fanwei Liang
affiliations:
- Independent Researcher
- South China University of Technology
arxiv_id: '2610.38610'
url: https://arxiv.org/abs/2610.38610
pdf_url: https://arxiv.org/pdf/2610.38610
published: '2026-10-28'
collected: '2026-10-30'
category: Agent
direction: Agent故障修复 · 评估错配
tags:
- LLM Agent
- Agent Failure Repair
- Evaluator-Executor Mismatch
- Rollout Verification
- Deployment Optimization
one_liner: 量化LLM Agent故障修复中评估者与执行者错配的损失，提出修复需用实际部署Agent验证
practical_value: '- 上线电商导购/客服Agent的故障修复策略时，禁止直接用离线大模型、greedy replay的评估结果上线，必须用实际部署的小模型做3~5次rollout验证，避免修复效果不及预期

  - 跨模型迁移修复策略、标注故障修复数据集时，必须明确标注数据对应的执行Agent，不要默认不同模型的最优修复选择一致

  - 资源有限时优先给部署Agent分配少量rollout预算，ROI远高于给更强评估模型分配多几倍的rollout预算

  - 做Agent相关benchmark时需明确标注评估所用的执行模型，避免不同研究者的结果不可复现'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent故障修复流程普遍用greedy replay、更强参数模型、环境oracle、LLM judge作为评估者筛选最优修复方案，隐含假设是评估者判定有效的修复对实际线上部署的执行Agent同样有效，但该假设从未被量化验证，评估与执行的模型错配可能导致修复效果大幅低于预期，甚至引入新的故障。
### 方法关键点
- 固定失败轨迹和单步候选修复集，以实际部署Agent的独立rollout结果作为最优修复的基准，定义选择损失为评估者选中修复与基准最优修复的部署价值差
- 实验覆盖3类交互环境（网格世界、ALFWorld家庭仿真、WebShop电商购物仿真），2类主流开源部署Agent（Qwen2.5-7B-Instruct、Llama-3.1-8B-Instruct），对比十几种工业界常用评估方案的损失
- 预注册全量实验方案，控制rollout预算、候选集偏差等干扰变量，避免数据窥探导致的结果偏置
### 关键结果
- 未筛选故障集上，greedy replay相对部署Agent自评估，在ALFWorld损失0.08~0.13的任务成功率，在WebShop损失0.06~0.13的用户reward
- 同等rollout预算下，用Qwen2.5-14B为Qwen2.5-7B选修复，ALFWorld成功率损失达0.25，20次14B的rollout评估效果不如2次7B自身的rollout
- 同量级不同家族模型互选修复，双向损失达0.07~0.17，部分错配场景下两个模型的最优修复偏好完全相反

**最值得记住的一句话：Agent故障修复没有通用最优解，最优修复选择完全依赖实际执行的模型，所有修复必须用最终部署的执行者做rollout验证后再上线**
