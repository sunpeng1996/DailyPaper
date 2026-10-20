---
title: 'OR-License: Evaluating LLM Agents as Real-World Operations Research Practitioners'
title_zh: OR-License：面向真实运筹学场景的LLM Agent专业能力基准评测
authors:
- Peisong Wang
- Feixue Liu
- Yize Meng
- Bowen Liu
- Ruoyu Chen
- Gaoyang Dai
- Xing He
- Aiqian Li
- Fengchi Yuan
- Aochuan Chen
affiliations:
- HKUST-GZ
- HKU
- Tencent Hunyuan
- Qingzhi Optimization
- XM Capital
arxiv_id: '2610.24087'
url: https://arxiv.org/abs/2610.24087
pdf_url: https://arxiv.org/pdf/2610.24087
published: '2026-10-15'
collected: '2026-10-20'
category: Agent
direction: Agent 专业能力基准评测 · 运筹学落地场景
tags:
- Agent
- Benchmark
- Operations Research
- LLM Evaluation
- Industrial Deployment
one_liner: 基于总价值368万美元的真实工业OR项目，构建端到端LLM Agent专业能力评测基准
practical_value: '- 做Agent落地评测可复用DAQ指标设计：先卡可行性再算质量，不可行直接得0分，符合工业场景上线要求，比单纯任务完成率更贴近实际业务价值

  - 开发长周期任务Agent时，可加入全流程信息获取触发机制：不要只在初始阶段做需求澄清，在中间结果验证、自测阶段也要触发需求校验逻辑，降低业务理解偏差

  - 复杂业务决策类Agent的错误分析可复用8类错误归因框架：从需求理解、约束建模到代码实现逐层排查，定位能力瓶颈更高效'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有OR领域LLM评测均基于预定义的标准化问题，省略了真实业务中需求澄清、信息补全、方案验证到最终交付的全流程环节，无法衡量LLM Agent能否替代专业OR从业者完成高价值付费工业项目，和实际落地场景存在显著gap。
### 方法关键点
- 数据集：筛选总价值368万美元的10个行业31个真实付费OR项目，脱敏后保留原始需求、输入格式、交付要求和信息差边界，无人工标准化改造
- 交互模拟：推出ORSIM客户端模拟器，Agent可在全流程任意阶段查询业务事实，但无法获得OR专业知识指导，完全对齐真实客户沟通边界
- 评测体系：提出**DAQ**指标，仅通过所有隐藏用例的可行方案才计入质量分，不可行交付直接得0分，专家验收通过的参考方案DAQ为1，更贴近工业落地要求
### 关键结果
评测11个前沿LLM搭配coding agent框架：最优Grok 4.6严格可行性88.39%，DAQ为0.87，所有模型均未达到专家水平；约86%的得分差距来自不可行交付，而非可行方案的质量差距；长周期任务的研究链（假设-实验-验证-迭代）完成率仅24%~45%。
### 核心结论
当前LLM Agent在复杂任务中的可靠交付能力缺口，远大于可行方案与专家的质量差距，长周期任务中持续补全信息差、验证假设的可靠性比单次推理能力更重要。
