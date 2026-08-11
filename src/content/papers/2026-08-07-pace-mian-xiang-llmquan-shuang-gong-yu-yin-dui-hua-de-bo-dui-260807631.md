---
title: 'PACE: A Playback-Aligned Context Engine for LLM-Based Full-Duplex Voice Dialogue'
title_zh: PACE：面向LLM全双工语音对话的播放对齐上下文引擎
authors:
- Shibo Wang
- Zicheng Zhang
- Libo Wang
- Junfeng Ma
affiliations:
- Alibaba Group
arxiv_id: '2608.07631'
url: https://arxiv.org/abs/2608.07631
pdf_url: https://arxiv.org/pdf/2608.07631
published: '2026-08-07'
collected: '2026-08-11'
category: Agent
direction: 语音对话Agent 全双工交互优化
tags:
- Full-Duplex Dialogue
- Context Alignment
- Middleware
- Referent Grounding
- Speech LLM
one_liner: 提出与模型无关的中间件PACE，解决全双工语音对话的生成上下文错锚问题，大幅提升指代锚定准确率
practical_value: '- 开发电商语音导购、智能客服等语音类Agent的全双工功能时，可直接复用PACE的中间件架构，无需修改底层LLM/语音模型即可解决用户打断时的上下文错配问题，降低开发成本

  - 对接黑盒大模型接口的场景，可借鉴「已播放音频重注入+固定提示语分隔符」的trick，无需模型开放上下文编辑、KV cache回滚能力即可实现上下文修正

  - 设计对话系统评测体系时，可参考GCM-Bench的构造思路，新增面向用户实际感知的指代锚定类用例，避免仅评测回复相关性忽略上下文对齐问题

  - 做交互类系统的状态设计时，可参考将客户端播放边界作为用户已接收内容代理的思路，避免用服务端生成状态替代用户实际感知状态的系统性错误'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
全双工语音对话允许用户打断助手回复，但服务端LLM生成速度远快于客户端播放速度，会触发生成上下文错锚（GCM）问题：用户基于已播放内容提问时，LLM会参考尚未播放的生成内容回复，导致指代错误、指令理解偏差，甚至错误执行不可逆操作（如电商下单、服务预约）。现有仅取消生成的方案无法修复已偏移的模型上下文，厂商专属的截断能力又绑定特定API，缺乏通用解决方案。
### 方法关键点
- 设计与模型/厂商无关的中间件层，核心通过`OutputTurnLedger`记录服务端生成的全量音频/文本，客户端持续上报`PlaybackAck`标记已播放样本边界，明确区分用户可感知和未感知的内容
- 中断触发时先快照播放边界、取消后续生成、撤回客户端未播放的缓冲内容，再基于runtime能力选择修复方式：级联系统直接重写对话历史，黑盒语音模型则提取已播放音频片段+固定提示语分隔符，和用户打断后的语音一起输入模型
- 构造GCM-Bench评测数据集，包含108个播放相关的指代锚定用例，覆盖不同场景、打断时机、指代操作，用于量化GCM修复效果
### 关键结果
- 对比仅取消生成的baseline，在GCM-Bench上指代锚定准确率（RAA）从25.0%提升至96.3%，其中`elaborate`类任务提升91.67pp
- 在200条Full-Duplex-Bench v1样本上，回复质量分从4.975微升至4.995，仅增加59ms平均响应延迟，无中断时完全不影响原有链路性能
> 最值得记住的结论：对话系统的上下文对齐永远要以用户实际可感知的内容为基准，而非服务端的生成进度
