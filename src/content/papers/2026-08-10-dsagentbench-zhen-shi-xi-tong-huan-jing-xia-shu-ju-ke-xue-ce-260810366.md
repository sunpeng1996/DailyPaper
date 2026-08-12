---
title: 'DSAgentBench: Can Agents Automate End-to-End Data-Science Workflows in Real
  Computer Environments?'
title_zh: DSAgentBench：真实系统环境下数据科学端到端工作流Agent评测基准
authors:
- Mizanur Rahman
- Mohammed Saidul Islam
- Ridwan Mahbub
- Md Tahmid Rahman Laskar
- Shafiq Joty
- Enamul Hoque Prince
affiliations:
- York University
- Nanyang Technological University
- Salesforce AI Research
arxiv_id: '2608.10366'
url: https://arxiv.org/abs/2608.10366
pdf_url: https://arxiv.org/pdf/2608.10366
published: '2026-08-10'
collected: '2026-08-12'
category: Agent
direction: Agent 端到端工作流能力评测
tags:
- Agent Benchmark
- Data Science Agent
- GUI Agent
- Multi-tool Orchestration
- Long-horizon Reasoning
one_liner: 首个支持真实操作系统交互的端到端数据科学工作流Agent评测基准，覆盖全流程多工具协同场景
practical_value: '- 构建业务Agent评测体系可复用其端到端结果校验逻辑，不局限于单步指令/代码正确性，覆盖跨数仓、BI工具、脚本的真实业务流程（如电商用户分析、报表生成Agent），采用确定性校验+LLM视觉校验结合的评估方式，更贴近业务真实需求

  - 开发长链路多工具Agent时优先优化环境grounding、工具编排、长程状态维护能力，从实验结果看这三类错误占比远高于单步推理错误，是当前Agent落地的核心瓶颈

  - 若业务场景需要Agent操作GUI工具（如商家后台、BI平台），可参考其扩展OSWorld对接专用工具的方案，快速搭建真实环境的Agent测试沙箱，降低调试成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有数据科学Agent评测存在明显缺陷：要么仅校验静态代码执行正确性，完全脱离真实操作系统交互；要么仅测试通用GUI操作能力，不覆盖数据科学全流程的跨工具协同、多步推理需求，无法真实反映Agent在实际业务场景中的可用能力。
### 方法关键点
- 基于OSWorld扩展数据科学专属环境：预装Ubuntu系统+Jupyter Notebook、VS Code、Chrome等常用工具，支持Kaggle、OpenML、SQLite等多源数据访问，完全还原真实工作流操作环境
- 构建275个人工标注的全链路任务，覆盖数据采集、EDA、特征工程、建模、评估、可视化6个核心阶段，其中56.7%为多阶段长流程任务，难度分层为难47.6%、中46.9%、易5.5%，匹配真实数据科学工作分布
- 采用结果导向的评估逻辑：不校验过程代码，仅对最终输出做确定性校验（数值类容忍合理精度误差），可视化类输出结合LLM视觉校验语义匹配度，评估结果更客观
### 关键实验结果
共测试15个闭源/开源Agent：最强闭源模型Claude-4.6-Sonnet搭配Screenshot+A11y Tree输入的任务成功率仅为56.7%，GPT-5为29.81%，其余闭源模型普遍在20%左右；所有开源Agent成功率均低于1%。人类执行相同任务的成功率为85.09%，当前Agent与人类能力存在巨大gap。
### 最值得记住的结论
当前Agent落地长链路跨工具业务场景的核心瓶颈不是单步推理能力，而是环境感知、工具编排、长程状态维护能力。
