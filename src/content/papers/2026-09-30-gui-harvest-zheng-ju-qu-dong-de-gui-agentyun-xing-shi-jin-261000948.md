---
title: 'GUI-HARVEST: Self-Improving GUI Agents through Evidence-Driven Harness Evolution'
title_zh: 《GUI-HARVEST：证据驱动的GUI Agent运行时Harness自进化框架》
authors:
- Geyi Yang
- Zikun Qu
- Xiang Li
- Zhiyong Wang
- Min Zhang
- Shipei Zeng
- Zhongxiang Dai
affiliations:
- 香港中文大学（深圳）
- 天津大学
- 哈尔滨工业大学（深圳）
- 华东师范大学
- 深圳大数据研究院
arxiv_id: '2610.00948'
url: https://arxiv.org/abs/2610.00948
pdf_url: https://arxiv.org/pdf/2610.00948
published: '2026-09-30'
collected: '2026-10-07'
category: Agent
direction: GUI Agent 运行时Harness自优化
tags:
- GUI Agent
- Harness Optimization
- Self-Improving Agent
- Multimodal Agent
- Cross-domain Transfer
one_liner: 冻结GUI Agent backbone，基于多模态执行证据自动优化运行时Harness实现跨任务性能提升
practical_value: '- 可复用「同任务多次执行聚类失败模式」的思路，优化电商导购Agent、店铺运营自动化Agent的运行时逻辑，无需调整大模型权重即可提升任务成功率

  - 多模态交互Agent迭代可借鉴「视觉证据+行为预测双校验」的变更上线机制，避免盲目上线带来的业务效果波动

  - Agent runtime优化可参考跨任务失败模式聚合生成代码补丁的方案，降低人工定制Harness的成本，同时提升补丁泛化性

  - 调用成本敏感的Agent场景，该方法优化后的Harness可在提升准确率的同时降低72%的API调用成本，适合电商大流量Agent落地'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有通用Agent Harness优化方法不适配GUI场景，存在三个核心痛点：模型意图与视觉执行效果不一致，文本日志显示成功但界面实际未完成；同任务多次执行结果波动，单次失败轨迹无法完整反映问题；单任务修复补丁难以泛化到其他任务。且冻结backbone做优化的需求迫切，尤其适合闭源模型、大模型微调成本高的场景。

### 方法关键点
- 证据分析模块：对齐模型输出、执行动作和前后截图，定位单任务多次执行中的行为差异，输出带证据支撑的失败结论
- 跨任务聚类模块：将多任务失败结论聚合成通用失败模式，避免单任务补丁过拟合
- Harness工程师模块：将失败模式转化为受限代码修改，提前记录补丁的预期行为效果方便后续校验
- 校验模块：通过「效用硬门控（搜索集、验证集得分不下降且至少一个有提升）+ 行为软门控（实际执行符合预期行为）」双重校验，仅通过有效补丁

### 关键实验
在OSWorld-Verified数据集上测试6款开源/闭源GUI backbone，相比初始Harness，Qwen3-VL-32B-Instruct全任务得分提升12.33个百分点；跨数据集迁移到WindowsAgentArena，GPT-5得分提升13.87个百分点；相比通用Harness优化方法Self-Harness、Meta-Harness，测试集得分分别多提升8.16、5.78个百分点，同时API调用成本降低72%。

**最值得记住的一句话**：对于GUI Agent，优化运行时Harness的投入产出比远高于微调大模型，且优化后的Harness可跨环境、跨任务泛化。
