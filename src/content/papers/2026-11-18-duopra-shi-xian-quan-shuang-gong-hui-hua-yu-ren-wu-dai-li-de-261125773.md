---
title: 'Duopra: From Full-Duplex Conversation to Full-Duplex Agency'
title_zh: Duopra：实现全双工会话与任务代理协同的交互模型
authors:
- Chiyu Chen
- Pengzhou Cheng
- Yuezhao Ma
- Xiaocheng Li
- Can Liu
- Haonan Hu
- Yao Yao
- Yifei Yang
- Yijie Lu
- Taolei Wang
affiliations:
- Shanghai Jiao Tong University
- Tencent
- Shanghai University
- University of Bristol
arxiv_id: '2611.25773'
url: https://arxiv.org/abs/2611.25773
pdf_url: https://arxiv.org/pdf/2611.25773
published: '2026-11-18'
collected: '2026-11-23'
category: Agent
direction: 全双工语音Agent · 工具调用优化
tags:
- Full-Duplex-Agent
- Tool-Calling
- SFT
- Reinforcement-Learning
- Voice-Assistant
one_liner: 提出三阶段训练的全双工交互模型，统一工具调用与后端委托接口，大幅提升任务成功率
practical_value: '- 做电商语音导购、智能客服这类语音Agent时，可将后端委托抽象为`query(task)`标准工具，统一直接调领域工具与委托后端的动作接口，省去独立分发器模块，降低架构复杂度

  - 三阶段训练流程可直接复用：先用SFT对齐工具调用协议，再用RL优化执行时效性、参数正确性，最后仅调整投影层修复语音生成质量，避免训练工具能力破坏原有会话交互效果

  - 全双工场景下任务成功率瓶颈在前端请求发起能力而非后端执行能力，优化前端的意图捕捉、参数修正、请求发起逻辑，收益远高于升级后端大模型规格'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有全双工交互模型仅具备会话控制能力，任务执行依赖前后端分离架构：前端仅负责转发请求给后端工具调用模块，但89%的任务失败源于前端未正确发起请求（未捕捉用户修正参数、未处理工具依赖顺序等），基线系统仅11%的会话会向后端发起有效请求，形成无法通过升级后端突破的成功率天花板。
### 方法关键点
- 统一动作空间：将后端委托抽象为参数为自然语言任务的`query(task)`标准工具，与直接调用领域工具共用同一套动作接口，无需独立路由模块
- 三阶段训练范式：1）协议SFT：微调模型思考层（thinker），学习工具schema调用、缺失参数澄清、结果上报逻辑；2）全双工RL：基于Dr.GRPO训练thinker的LoRA适配器，奖励及时、完整、事实 grounded 的执行，惩罚使用用户已修正的参数；3）仅投影层修复：冻结训练完成的thinker，仅调整thinker到语音生成层（talker）的投影层，对齐原有会话的隐藏态分布，避免语音质量下降
### 关键结果
在FDB v3全双工工具调用基准上测试：
- 相同Qwen3-8B后端下，Pass@1从基线的4.7%提升至44.7%；直接调用领域工具时Pass@1达47.7%，搭配DeepSeek后端时Pass@1达49.3%
- FDB v1.0的三项会话接管率（用户说完接话、暂停不抢话、被中断后停止）均优于基线，投影层修复后语音识别错误率下降超50%
### 核心结论
全双工Agent的任务成功瓶颈首先在请求发起能力，执行可以卸载，但发起准确请求的责任永远在前端
