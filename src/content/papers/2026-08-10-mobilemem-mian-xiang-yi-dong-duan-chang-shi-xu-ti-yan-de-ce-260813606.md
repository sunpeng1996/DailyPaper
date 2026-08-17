---
title: 'MobileMem: Learning from a Year of Mobile Experiences'
title_zh: MobileMem：面向移动端长时序体验的端侧长期记忆基准与框架
authors:
- Xinle Deng
- Yida Xue
- Xiangyuan Ru
- Haoming Xu
- Shuofei Qiao
- Mengru Wang
- Yijun Chen
- Buqiang Xu
- Chen Jiang
- Yuchen Eleanor Jiang
affiliations:
- OPPO
- OpenKG
- Zhejiang University
arxiv_id: '2608.13606'
url: https://arxiv.org/abs/2608.13606
pdf_url: https://arxiv.org/pdf/2608.13606
published: '2026-08-10'
collected: '2026-08-17'
category: Agent
direction: Agent端侧长时记忆基准构建
tags:
- On-Device-Agent
- Long-Term-Memory
- Benchmark
- Experience-Synthesis
- Personal-Intelligence
one_liner: 提出面向移动端场景的长时记忆基准MobileMem与知识引导的体验合成框架KEME
practical_value: '- 做端侧个性化推荐/个人Agent时可复用双层内存架构：系统层存跨APP全局偏好，应用层做领域内记忆过滤，仅上报高价值结构化事件，降低端侧存储计算开销同时提升隐私性

  - 长时序用户行为数据不足时，可复用KEME的知识引导合成框架，基于真实用户persona和时序约束生成高一致性的长周期交互轨迹，降低数据采集成本和隐私风险

  - 长时记忆系统选型可参考实验结论：A-MEM和HippoRAG2在多跳、时序推理任务上表现最优（整体准确率~80%），但需承担更高token开销，端侧部署可优先权衡性能与成本

  - 端侧记忆系统的对抗性鲁棒性优化可参考LangMem的设计思路，避免弱相关记忆引入的误判问题，提升无答案场景的拒答准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent长时记忆基准多面向云侧场景，未适配移动端数据异构、多模态、时序连续、隐私敏感、存储算力受限的特性，无法支撑端侧持久化个人智能的开发与评估，同时长周期真实用户移动交互数据采集成本高、隐私风险大，缺乏标准化合成方案。

### 方法关键点
- 提出双层端侧内存架构：系统级内存层作为黑板存储跨APP全局用户状态，应用级内存层做认知卸载，仅向系统层上报高价值结构化事件，通过标准化协议实现信息交互，兼顾扩展性与隐私性
- 提出KEME知识引导的体验合成框架：以用户persona、真实交互元数据为知识锚点，通过4个专用Agent交替做顶部时序规划和底部体验演化，生成时序一致的长周期用户交互轨迹，同时自底向上生成多类型QA对
- 构建两个互补基准：纯文本的MobileMem（覆盖7类APP交互）和多模态的MobileMem-Omni（覆盖截图等视觉信息），覆盖多跳推理、时序推理、知识更新、隐式偏好推断等核心记忆能力评估

### 关键结果
在MobileMem基准上对比10种主流记忆系统，A-MEM和HippoRAG2整体表现最优，搭配GPT-4.1-mini时准确率分别达79.68%和78.85%；两类模型在时序推理、查询摘要任务上性能显著低于单跳任务（普遍下降15~25个百分点），是当前记忆系统的核心瓶颈；长上下文方案性能仅54.51%，且受窗口大小限制严重。

最值得记住的一句话：端侧记忆是下一代个人智能的核心差异化竞争力，未来每个用户的专属AI都需要独立的端侧内存层作为基础设施。
