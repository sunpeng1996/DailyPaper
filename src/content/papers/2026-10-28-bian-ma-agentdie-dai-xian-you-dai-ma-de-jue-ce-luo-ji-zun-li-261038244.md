---
title: Precedent or Intent? What Coding Agents Follow When Evolving Existing Code
title_zh: 编码Agent迭代现有代码的决策逻辑：遵循历史惯例还是新意图
authors:
- Haichao Zhu
- Geyang Xu
- Zhaorui Yang
- Jiyuan Wang
- Qian Zhang
affiliations:
- University of California, Riverside
- Independent Researcher
- Tulane University
arxiv_id: '2610.38244'
url: https://arxiv.org/abs/2610.38244
pdf_url: https://arxiv.org/pdf/2610.38244
published: '2026-10-28'
collected: '2026-10-30'
category: Agent
direction: 编码Agent 决策优先级机制研究
tags:
- Coding Agent
- Software Evolution
- LLM Decision Making
- Precedent Priority
- Task Guidance
one_liner: 通过5625次受控实验揭示编码Agent对历史惯例、新任务规则的决策优先级规律
practical_value: '- 搭建业务自动化Agent（如推荐规则迭代、商品上新、广告素材生成Agent）时，若要让Agent跳出历史惯例遵循新要求，必须显式写入优先级规则，仅提供参考样例的可靠性低35%以上

  - 给Agent喂参考上下文时，优先召回当前修改模块的本地相关文件，跨模块的兄弟文件参考价值极低，无需浪费token加载，相同数量的本地样例影响力是跨模块的24倍

  - 做Agent的RAG或prompt优化时，相同数量的参考样例，放在和当前任务更相关的位置（如本地文件、任务说明开头），效果远好于堆数量，调整位置即可实现0-100%的采纳率变化'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM编码Agent已广泛参与代码迭代任务，但现有代码仅记录历史实现选择，不会保留决策背后的 rationale，当历史实现惯例与新任务意图冲突时，Agent的决策逻辑不透明，可能导致生成代码不符合业务规范、引入隐形一致性问题。
### 方法关键点
- 三阶段受控实验设计，分别隔离三大影响因素：Agent无参考时的默认偏好、仓库不同位置的历史惯例、显式任务指导的优先级
- 构造6组功能完全等价的实现对（如ID序列化整数/字符串、错误处理返回/抛出、命名snake_case/camelCase等），保证功能测试通过率与实现选择完全解耦
- 区分本地（当前修改资源的关联文件）与兄弟资源（其他模块文件）的惯例，控制样例数量、放置位置两个变量，单独测量各自影响
### 关键实验结果
累计5625次试验，覆盖4个主流编码Agent、6组实现对，同时在4个跨Python/Go/TypeScript的开源仓库做验证：
1. 历史惯例与Agent默认偏好冲突时，359/360次试验Agent选择遵循惯例
2. 相同数量样例，本地文件惯例采纳率96%，兄弟资源文件仅4%，仅调整样例放置位置即可将采纳率从0%拉到100%
3. 显式优先级规则对抗冲突惯例的成功率98%（59/60），仅提供代码示例成功率仅63%（38/60）；开源仓库中，harness加载的规则可将任务成功率从0/120提升到117/120
### 最值得记住的结论
要让Agent偏离历史惯例遵循新意图，不要仅提供示例，必须显式声明优先级规则，且优先提供当前模块的本地参考样例
